from uuid import uuid4
from database import db


class CommentLikes(db.Model):
    __tablename__ = 'comment_likes'

    # Foreign Key
    id = db.Column(db.String(36), default=lambda: str(uuid4()), primary_key=True)
    comment_id = db.Column(db.String(36), db.ForeignKey('comments.id'))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'))
    cooperative_id = db.Column(db.String(36), db.ForeignKey('cooperative.id'))

    def serialize(self):
        return {
                'id': self.id,
                'user_id': self.user_id,
                'cooperative_id': self.cooperative_id,
                'comment_id': self.comment_id,
                'active': self.active
                }
