import json

from flask import jsonify

from dao.models.user import User


class AuthDAO:
    def __init__(self, session):
        self.session = session

    def get_find_username(self, username):
        """Ищем пользователя"""
        user = self.session.query(User).filter(User.username == username).first()
        data = {
            "username": user.username,
            "role": user.role,
            "password": user.password
        }
        return data
