from uuid import uuid4
from database import db
from app.models.type_of_garbage import TypeOfGarbage


class Garbage(db.Model):
    __tablename__ = 'garbage'

    # Columns
    id = db.Column(db.String(36), default=lambda: str(uuid4()), primary_key=True)
    ds_url = db.Column(db.String(500), nullable=True)
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    type_of_garbage = db.Column(db.String(15), nullable=False)
    active = db.Column(db.Boolean(), default=True)

    def type(self):
        _type = TypeOfGarbage()
        return _type.get_type(self.type_of_garbage.lower())

    def serialize(self):
        return {
                'id': self.id,
                'name': self.name,
                'description': self.description,
                'type_of_garbage': self.type(),
                'name_type': self.type_of_garbage,
                'ds_url': self.ds_url,
                'active': self.active
                }
