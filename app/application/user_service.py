from app.domain.models import User
from app.domain.repositories import AbstractUserRepository

class UserService:
    def __init__(self, repo: AbstractUserRepository):
        self.repo = repo

    def create_user(self, username: str) -> User:
        return self.repo.create(User(id=0, username=username))

    def get_user(self, user_id: int) -> User:
        return self.repo.get_by_id(user_id)
    