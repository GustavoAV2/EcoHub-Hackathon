import jwt
from typing import Dict, List
from datetime import timedelta, datetime
from app.models.entities.users import User
from flask_jwt_extended import create_access_token
from database.repository import save, delete, commit
from werkzeug.security import generate_password_hash


def login_user(email, password) -> Dict or None:
    try:
        user = get_user_by_email(email)

        if user:
            if not user.verify_password(password) or not user.active:
                return

            token = jwt.encode(user.serialize(), "secret", algorithm="HS256")
            return {"access_token": token, 'username': user.name}
    except (AttributeError, KeyError, TypeError):
        return


def create_user(data: Dict) -> User or None:
    try:
        return save(User(
            name=data.get('name'),
            email=data.get('email'),
            password=generate_password_hash(data.get('password')),
            cep=data.get('cep'),
            address=data.get('address'),
            complement=data.get('complement'),
            cpf=data.get('cpf'),
            birth_date=datetime.strptime(data.get('birth_date'), "%Y-%m-%d"),
            active=data.get('active')
        ))
    except (AttributeError, KeyError, TypeError):
        return


def update_user(user_id: str, data: Dict) -> User:
    user: User = get_user_by_id(user_id)
    list_keys = list(data.keys())

    user.email = data.get('email') if data.get('email') else user.email
    user.active = data.get('active') if list_keys.count('active') else user.active
    user.password = generate_password_hash(data.get('password')) if data.get('password') else user.password
    user.name = data.get('name') if data.get('name') else user.name
    user.cep = data.get('cep') if data.get('cep') else user.cep
    user.address = data.get('address') if data.get('address') else user.address
    user.complement = data.get('complement') if data.get('complement') else user.complement
    user.cpf = data.get('cpf') if data.get('cpf') else user.cpf
    user.birth_date = data.get('birth_date') if data.get('birth_date') else user.birth_date

    commit()
    return user


def deleted_user(user_id: str) -> User:
    user: User = get_user_by_id(user_id)
    delete(user)
    commit()
    return user


def get_users() -> List[User]:
    users = User.query.all()
    return users


def get_user_by_id(user_id: str) -> User:
    return User.query.get(user_id)


def get_user_by_email(email: str) -> User:
    return User.query.filter(User.email == email).first()
