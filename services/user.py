from dao.user import UserDAO
from function import get_hash


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_id(self, nid):
        return self.dao.get_id(nid)

    def create(self, data):
        data["password"] = get_hash(data["password"])
        self.dao.create(data)

    def update(self, data):
        self.dao.update(data)

    def delete(self, nid):
        self.dao.delete(nid)
