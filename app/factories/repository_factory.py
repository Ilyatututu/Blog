from sqlalchemy.orm import Session
from app.infrastructure.repositories import SQLPostRepository, SQLUserRepository, SQLCommentRepository
from app.domain.repositories import AbstractPostRepository, AbstractUserRepository, AbstractCommentRepository

class RepositoryFactory:
    @staticmethod
    def create_post_repository(db: Session) -> AbstractPostRepository:
        return SQLPostRepository(db)
    
    @staticmethod
    def create_user_repository(db: Session) -> AbstractUserRepository:
        return SQLUserRepository(db)

    @staticmethod
    def create_comment_repository(db: Session) -> AbstractCommentRepository:
        return SQLCommentRepository(db)