from flask import request, abort
from flask_restx import Resource, Namespace
from container import user_service
from dao.models.user import UserSchema

user_ns = Namespace('users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route("/")
class UserView(Resource):
    # def get(self):
    #     args = request.args
    #     if 'director_id' in args:
    #         mov = movie_service.get_director_id(args.get('director_id'))
    #     elif 'genre_id' in args:
    #         mov = movie_service.get_genre_id(args.get('genre_id'))
    #     elif 'year' in args:
    #         mov = movie_service.get_movie_year(args.get('year'))
    #     else:
    #         mov = movie_service.get_all()
    #     return movies_schema.dump(mov), 200

    def post(self):
        user = request.json
        user_service.create(user)
        return "", 201


@user_ns.route("/<int:nid>")
class UserView(Resource):
    def get(self, nid):
        movie = user_service.get_id(nid)
        if movie is None:
            abort(404)
        return user_schema.dump(movie), 200

    def delete(self, nid: int):
        user_service.delete(nid)
        return "", 204

    def put(self):
        user = request.json
        user_service.create(user)
        return "", 401


@user_ns.route("/auth/")
class UserView(Resource):
    def post(self):
        user = request.json
        return user_service.create(user)
 #       return "", 401

    def put(self):
        user = request.json
        user_service.create(user)
        return "", 401
