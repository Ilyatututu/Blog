from abc import ABC, abstractmethod
from typing import List
from .models import Post, User, Comment

class AbstractPostRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Post]: pass

    @abstractmethod
    def create(self, post: Post) -> Post: pass

class AbstractUserRepository(ABC):
    @abstractmethod
    def create(self, user: User) -> User: pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> User: pass

class AbstractCommentRepository(ABC):
    @abstractmethod
    def get_all_by_post(self, post_id: int) -> List[Comment]: pass

    @abstractmethod
    def create(self, comment: Comment) -> Comment: pass
    