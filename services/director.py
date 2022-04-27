from dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self):
        director_all = self.dao.get_all()
        return director_all

    def get_id(self, nid):
        director = self.dao.get_id(nid)
        return director

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)

    def delete(self, nid):
        self.dao.delete(nid)
