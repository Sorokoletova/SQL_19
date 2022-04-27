from dao.models.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        director_all = self.session.query(Director)
        return director_all

    def get_id(self, nid):
        director = self.session.query(Director).filter(Director.id == nid).first()
        return director

    def create(self, data):
        director = Director(**data)
        self.session.add(director)
        self.session.commit()
        return director

    def update(self, data):
        nid = data.get("id")
        self.session.query(Director).filter(Director.id == nid).update(data)
        self.session.commit()

    def delete(self, nid):
        director = self.session.query(Director).filter(Director.id == nid).first()
        self.session.delete(director)
        self.session.commit()
