from flask import request, abort
from flask_restx import Resource, Namespace

from container import movie_service
from dao.models.movie import MovieSchema
from function import auth_required, admin_required

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route("/")
class MovieView(Resource):
    @auth_required
    def get(self):
        args = request.args
        if 'director_id' in args:
            mov = movie_service.get_director_id(args.get('director_id'))
        elif 'genre_id' in args:
            mov = movie_service.get_genre_id(args.get('genre_id'))
        elif 'year' in args:
            mov = movie_service.get_movie_year(args.get('year'))
        else:
            mov = movie_service.get_all()
        return movies_schema.dump(mov), 200

    @admin_required
    def post(self):
        movie = request.json
        movie_service.create(movie)
        return "", 201


@movie_ns.route("/<int:nid>")
class MovieView(Resource):
    @auth_required
    def get(self, nid):
        movie = movie_service.get_id(nid)
        if movie is None:
            abort(404)
        return movie_schema.dump(movie), 200

    @admin_required
    def put(self, nid: int):
        movie = request.json
        movie['id'] = nid
        movie_service.update(movie)
        return "", 204

    @admin_required
    def delete(self, nid: int):
        movie_service.delete(nid)
        return "", 204
