from typing import Dict, List
from datetime import timedelta
from app.models.entities.cooperative import Cooperative
from flask_jwt_extended import create_access_token
from database.repository import save, delete, commit
from werkzeug.security import generate_password_hash


def login_coop(email, password) -> Dict or None:
    try:
        cooperative = get_cooperative_by_email(email)

        if cooperative:
            if not cooperative.verify_password(password) or not cooperative.active:
                return

            access_token = create_access_token(identity=cooperative.id, expires_delta=timedelta(minutes=600))
            return {'access_token': access_token}
    except (AttributeError, KeyError, TypeError):
        return


def create_cooperative(data: Dict) -> Cooperative or None:
    try:
        return save(Cooperative(
            name=data.get('name'),
            email=data.get('email'),
            password=generate_password_hash(data.get('password')),
            cep=data.get('cep'),
            address=data.get('address'),
            complement=data.get('complement'),
            cpf=data.get('cpf'),
            birth_date=data.get('birth_date'),
            active=data.get('active'),
            type_of_garbage_accepted=data.get('type_of_garbage_accepted'),  # List[TypeOfGarbage]
            preferencial_garbage=data.get('preferencial_garbage')  # List[Garbage]
        ))
    except (AttributeError, KeyError, TypeError):
        return


def update_cooperative(cooperative_id: str, data: Dict) -> Cooperative:
    cooperative: Cooperative = get_cooperative_by_id(cooperative_id)
    list_keys = list(data.keys())

    cooperative.email = data.get('email') if data.get('email') else cooperative.email
    cooperative.active = data.get('active') if list_keys.count('active') else cooperative.active
    cooperative.password = generate_password_hash(data.get('password')) if data.get('password') else cooperative.password
    cooperative.name = data.get('name') if data.get('name') else cooperative.name
    cooperative.cep = data.get('cep') if data.get('cep') else cooperative.cep
    cooperative.address = data.get('address') if data.get('address') else cooperative.address
    cooperative.complement = data.get('complement') if data.get('complement') else cooperative.complement
    cooperative.cpf = data.get('cpf') if data.get('cpf') else cooperative.cpf
    cooperative.birth_date = data.get('birth_date') if data.get('birth_date') else cooperative.birth_date

    commit()
    return cooperative


def deleted_cooperative(cooperative_id: str) -> Cooperative:
    cooperative: Cooperative = get_cooperative_by_id(cooperative_id)
    delete(cooperative)
    commit()
    return cooperative


def get_cooperative() -> List[Cooperative]:
    cooperatives = Cooperative.query.all()
    return cooperatives


def get_cooperative_by_id(cooperative_id: str) -> Cooperative:
    return Cooperative.query.get(cooperative_id)


def get_cooperative_by_email(email: str) -> Cooperative:
    return Cooperative.query.filter_by(email=email).first()
