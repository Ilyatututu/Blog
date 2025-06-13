from typing import List
from app.domain.models import Comment
from app.domain.repositories import AbstractCommentRepository

class CommentService:
    def __init__(self, repo: AbstractCommentRepository):
        self.repo = repo

    def get_comments(self, post_id: int) -> List[Comment]:
        return self.repo.get_all_by_post(post_id)

    def create_comment(self, post_id: int, author_id: int, content: str) -> Comment:
        return self.repo.create(Comment(id=0, post_id=post_id, author_id=author_id, content=content))
    
    def delete_comment(self, comment_id: int) -> bool:
        return self.repo.delete(comment_id)