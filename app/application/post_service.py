from typing import List
from app.domain.models import Post
from app.domain.repositories import AbstractPostRepository

class PostService:
    def __init__(self, repo: AbstractPostRepository):
        self.repo = repo

    def list_posts(self) -> List[Post]:
        return self.repo.get_all()

    def create_post(self, title: str, content: str, author_id: int) -> Post:
        return self.repo.create(Post(id=0, title=title, content=content, author_id=author_id))
    