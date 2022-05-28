from typing import Dict, List
from app.models.entities.garbage import Garbage
from database.repository import save, delete, commit
from app.models.type_of_garbage import TypeOfGarbage


def create_garbage(data: Dict, ds_url) -> Garbage or None:
    _type = TypeOfGarbage()
    # try:
    return save(Garbage(
        name=data.get('name'),
        description=data.get('description'),
        active=data.get('active'),
        ds_url=ds_url,
        type_of_garbage=_type.get_type(data.get('type')).get('name')
    ))
    # except (AttributeError, KeyError, TypeError):
    #     return


def update_garbage(garbage_id: str, data: Dict) -> Garbage:
    garbage: Garbage = get_garbage_by_id(garbage_id)
    list_keys = list(data.keys())

    garbage.name = data.get('name') if data.get('name') else garbage.name
    garbage.description = data.get('description') if data.get('description') else garbage.description
    garbage.active = data.get('active') if list_keys.count('active') else garbage.active
    garbage.description = data.get('description') if data.get('description') else garbage.description

    commit()
    return garbage


def delete_garbage(garbage_id: str) -> Garbage:
    garbage: Garbage = get_garbage_by_id(garbage_id)
    delete(garbage)
    commit()
    return garbage


def get_garbage() -> List[Garbage]:
    list_garbage = Garbage.query.all()
    return list_garbage


def get_garbage_by_type(type_of_garbage) -> List[Garbage]:
    list_garbage = Garbage.query.filter_by(type_of_garbage=type_of_garbage).all()
    return list_garbage


def get_garbage_by_id(garbage_id: str) -> Garbage:
    return Garbage.query.get(garbage_id)


def get_garbage_by_name(garbage_name: str) -> List[Garbage]:
    name = "%{}%".format(garbage_name)
    return Garbage.query.filter(Garbage.name.like(name)).all()
