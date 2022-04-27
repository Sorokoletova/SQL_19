import base64
import hashlib
from datetime import timedelta, datetime
import jwt
from flask import request
from flask_restx import abort

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS, PWD_HASH_NAME, SECRET, AlGORITM


def get_hash(password):
    """Хешируем пароль"""
    new_password = hashlib.pbkdf2_hmac(
        hash_name=PWD_HASH_NAME,
        password=password.encode('utf-8'),
        salt=PWD_HASH_SALT,
        iterations=PWD_HASH_ITERATIONS)
    return base64.b64encode(new_password).decode('utf-8')


# print(get_hash('my_little_pony'))

def generate_tokens(data):
    """Создаем пару токенов"""
    data['exp'] = datetime.utcnow() + timedelta(minutes=30)
    data['refresh_token'] = False
    access_token = jwt.encode(payload=data, key=SECRET, algorithm=AlGORITM)
    data['exp'] = datetime.utcnow() + timedelta(days=60)
    data['refresh_token'] = True
    refresh_token = jwt.encode(payload=data, key=SECRET, algorithm=AlGORITM)
    tokens_user = {"access_token": access_token, "refresh_token": refresh_token}

    return tokens_user, 201


def decode_tokens(token):
    """Раскодируем токен"""
    dec_token = {}
    try:
        dec_token = jwt.decode(jwt=token, key=SECRET, algorithms=[AlGORITM])
    except Exception as e:
        print("JWT Decode Exception", e)
        abort(401)

    return dec_token


def auth_required(func):
    """Декоратор проверки на аутентификацию"""
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        token = request.headers["Authorization"].split(" ")[-1]
        try:
            jwt.decode(jwt=token, key=SECRET, algorithms=[AlGORITM])
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    """Декоратор проверки на роль admin"""
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401)

        token = request.headers["Authorization"].split(" ")[-1]
        role = None

        try:
            user = decode_tokens(token)
            role = user["role"]
        except Exception as e:
            print("JWT Decode Exception", e)
            abort(401)

        if role != "admin":
            abort(403)

        return func(*args, **kwargs)

    return wrapper
