from typing import List
from app.domain.models import User
from app.domain.repositories import AbstractUserRepository

class UserService:
    def __init__(self, repo: AbstractUserRepository):
        self.repo = repo

    def get_users(self) -> List[User]:
        return self.repo.get_all()

    def create_user(self, username: str) -> User:
        return self.repo.create(User(id=0, username=username))
    
    def delete_user(self, user_id: int) -> bool:
        return self.repo.delete(user_id)