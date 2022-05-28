from uuid import uuid4
from database import db
from datetime import datetime
from sqlalchemy.orm import backref


class Comments(db.Model):
    __tablename__ = 'comments'

    # Foreign Key
    garbage_id = db.Column(db.String(36), db.ForeignKey('garbage.id'))
    user_id = db.Column(db.String(36), db.ForeignKey('users.id'))
    cooperative_id = db.Column(db.String(36), db.ForeignKey('cooperative.id'))
    user = db.relationship("User", backref=backref("users", uselist=False))

    comment_liked = db.relationship("CommentLikes", backref=backref("comment_likes", uselist=True))

    # Columns
    id = db.Column(db.String(36), default=lambda: str(uuid4()), primary_key=True)
    message = db.Column(db.String(1500), default=lambda: str(uuid4()))
    creation_date = db.Column(db.Date(), default=datetime.utcnow)
    active = db.Column(db.Boolean(), default=True)

    @property
    def likes(self):
        return len(self.comment_liked)

    def serialize(self):
        return {
                'id': self.id,
                'message': self.message,
                'up_votes': len(self.comment_liked),
                'user': self.user.serialize() if self.user else None,
                'user_id': self.user_id,
                'username': self.user.name if self.user else None,
                'garbage_id': self.garbage_id,
                'cooperative_id': self.cooperative_id,
                'is_coop': True if self.cooperative_id else False,
                'creation_date': self.creation_date,
                'active': self.active
                }
