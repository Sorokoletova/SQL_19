from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self):
        return self.dao.get_all()

    def get_id(self, nid):
        return self.dao.get_id(nid)

    def get_director_id(self, director_id):
        return self.dao.get_director_id(director_id)

    def get_genre_id(self, genre_id):
        return self.dao.get_genre_id(genre_id)

    def get_movie_year(self, year):
        return self.dao.get_movie_year(year)

    def create(self, data):
        return self.dao.create(data)

    def update(self, data):
        self.dao.update(data)

    def delete(self, nid):
        self.dao.delete(nid)
