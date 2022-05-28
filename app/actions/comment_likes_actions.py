from typing import Dict, List
from database.repository import save
from app.models.entities.comment_likes import CommentLikes


def create_like_comment(comment_id, cooperative_id="", user_id="") -> CommentLikes or None:
    try:
        return save(CommentLikes(
            comment_id=comment_id,
            cooperative_id=cooperative_id,
            user_id=user_id
        ))
    except (AttributeError, KeyError, TypeError):
        return


def get_like_comments() -> List[CommentLikes]:
    list_comment = CommentLikes.query.all()
    return list_comment
