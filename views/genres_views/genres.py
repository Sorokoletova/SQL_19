from flask import abort, request
from flask_restx import Resource, Namespace

from container import genre_service
from dao.models.genre import GenreSchema
from function import auth_required, admin_required

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route("/")
class GenreView(Resource):
    @auth_required
    def get(self):
        all_genre = genre_service.get_all()
        return genres_schema.dump(all_genre), 200

    @admin_required
    def post(self):
        genre = request.json
        genre_service.create(genre)
        return "", 201


@genre_ns.route("/<int:nid>")
class GenreView(Resource):
    @auth_required
    def get(self, nid):
        genre = genre_service.get_id(nid)
        if genre is None:
            abort(404)
        return genre_schema.dump(genre), 200

    @admin_required
    def put(self, nid: int):
        genre = request.json
        genre['id'] = nid
        genre_service.update(genre)
        return "", 204

    @admin_required
    def delete(self, nid: int):
        genre_service.delete(nid)
        return "", 204
