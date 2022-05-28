from typing import Dict, List
from app.models.entities.comments import Comments
from database.repository import save, delete, commit


def create_comment(data: Dict, garbage_id, cooperative_id="", user_id="") -> Comments or None:
    try:
        return save(Comments(
            message=data.get('message'),
            garbage_id=garbage_id,
            cooperative_id=cooperative_id,
            user_id=user_id,
            active=data.get('active')
        ))
    except (AttributeError, KeyError, TypeError):
        return


def update_comment(comment_id: str, data: Dict) -> Comments:
    comment: Comments = get_comment_by_id(comment_id)
    list_keys = list(data.keys())

    comment.message = data.get('message') if data.get('message') else comment.message
    comment.is_coop = data.get('is_coop') if data.get('is_coop') else comment.is_coop
    comment.user_id = data.get('user_id') if data.get('user_id') else comment.user_id
    comment.post_id = data.get('post_id') if list_keys.count('post_id') else comment.post_id
    comment.active = data.get('active') if list_keys.count('active') else comment.active

    commit()
    return comment


def delete_comment(comment_id: str) -> Comments:
    comment: Comments = get_comment_by_id(comment_id)
    delete(comment)
    commit()
    return comment


def get_comments() -> List[Comments]:
    list_comment = Comments.query.all()
    return list_comment


def get_comment_by_id(comment_id: str) -> Comments:
    return Comments.query.get(comment_id)


def get_comment_by_garbage_id(garbage_id: str) -> List[Comments]:
    return Comments.query.filter_by(garbage_id=garbage_id).all()


def get_comment_sort_by_up_votes() -> List[Comments]:
    comments = get_comments()
    for comment in comments:
        print(comment)
