from dao.models.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_id(self, nid):
        user = self.session.query(User).filter(User.id == nid).first()
        return user

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, data):
        nid = data.get("id")
        self.session.query(User).filter(User.id == nid).update(data)
        self.session.commit()

    def delete(self, nid):
        user = self.session.query(User).filter(User.id == nid).first()
        self.session.delete(user)
        self.session.commit()
