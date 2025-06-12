from sqlalchemy.orm import Session
from app.domain.models import Post, User, Comment
from app.domain.repositories import AbstractPostRepository, AbstractUserRepository, AbstractCommentRepository
from .models import PostDB, UserDB, CommentDB

class SQLPostRepository(AbstractPostRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        db_posts = self.db.query(PostDB).all()
        return [Post(id=p.id, title=p.title, content=p.content, author_id=p.author_id)
                for p in db_posts]

    def create(self, post: Post):
        db_post = PostDB(title=post.title, content=post.content, author_id=post.author_id)
        self.db.add(db_post)
        self.db.commit()
        self.db.refresh(db_post)
        return Post(id=db_post.id, title=db_post.title, content=db_post.content, author_id=db_post.author_id)
    
class SQLUserRepository(AbstractUserRepository):
    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        db_user = UserDB(username=user.username)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return User(id=db_user.id, username=db_user.username)

    def get_by_id(self, user_id: int) -> User:
        db_user = self.db.query(UserDB).filter(UserDB.id == user_id).first()
        if db_user:
            return User(id=db_user.id, username=db_user.username)
        return None

class SQLCommentRepository(AbstractCommentRepository):
    def __init__(self, db: Session):
        self.db = db

    def get_all_by_post(self, post_id: int):
        db_comments = self.db.query(CommentDB).filter(CommentDB.post_id == post_id).all()
        return [Comment(id=c.id, content=c.content, post_id=c.post_id, author_id=c.author_id) for c in db_comments]

    def create(self, comment: Comment) -> Comment:
        db_comment = CommentDB(content=comment.content, post_id=comment.post_id, author_id=comment.author_id)
        self.db.add(db_comment)
        self.db.commit()
        self.db.refresh(db_comment)
        return Comment(id=db_comment.id, content=db_comment.content, post_id=db_comment.post_id, author_id=db_comment.author_id)