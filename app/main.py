from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.infrastructure.models import Base
from app.factories.repository_factory import RepositoryFactory
from app.application.post_service import PostService
from app.application.user_service import UserService
from app.application.comment_service import CommentService

DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/posts")
def get_posts(db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    return service.get_posts()

@app.get("/comments")
def get_comments(post_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    return service.get_comments(post_id)

@app.get("/users")
def get_users(db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    return service.get_users()

@app.post("/posts")
def create_post(title: str, content: str, author_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    return service.create_post(title, content, author_id)

@app.post("/users")
def create_user(username: str, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    return service.create_user(username)

@app.post("/comments")
def create_comment(post_id: int, author_id: int, content: str, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    return service.create_comment(post_id, author_id, content)

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_post_repository(db)
    service = PostService(repo)
    if not service.delete_post(post_id):
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_user_repository(db)
    service = UserService(repo)
    if not service.delete_user(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}

@app.delete("/comments/{comment_id}")
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    repo = RepositoryFactory.create_comment_repository(db)
    service = CommentService(repo)
    if not service.delete_comment(comment_id):
        raise HTTPException(status_code=404, detail="Comment not found")
    return {"message": "Comment deleted"}
