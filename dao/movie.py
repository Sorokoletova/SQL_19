from dao.models.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        movies_all = self.session.query(Movie)
        return movies_all

    def get_id(self, nid):
        movie = self.session.query(Movie).filter(Movie.id == nid).first()
        return movie

    def get_director_id(self, director_id):
        movie_director = self.session.query(Movie).filter(Movie.director_id == director_id).all()
        return movie_director

    def get_genre_id(self, genre_id):
        movie_genre = self.session.query(Movie).filter(Movie.genre_id == genre_id).all()
        return movie_genre

    def get_movie_year(self, year):
        movie_year = self.session.query(Movie).filter(Movie.year == year).all()
        return movie_year

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def update(self, data):
        nid = data.get("id")
        self.session.query(Movie).filter(Movie.id == nid).update(data)
        self.session.commit()

    def delete(self, nid):
        movie = self.session.query(Movie).filter(Movie.id == nid).first()
        self.session.delete(movie)
        self.session.commit()
