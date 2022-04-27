from flask import abort, request
from flask_restx import Resource, Namespace
from container import director_service
from dao.models.director import DirectorSchema
from function import auth_required, admin_required

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)


@director_ns.route("/")
class DirectorView(Resource):
    @auth_required
    def get(self):
        all_director = director_service.get_all()
        return directors_schema.dump(all_director), 200

    @admin_required
    def post(self):
        director = request.json
        director_service.create(director)
        return "", 201


@director_ns.route("/<int:nid>")
class DirectorView(Resource):
    @auth_required
    def get(self, nid):
        director = director_service.get_id(nid)
        if director is None:
            abort(404)
        return director_schema.dump(director), 200

    @admin_required
    def put(self, nid: int):
        director = request.json
        director['id'] = nid
        director_service.update(director)
        return "", 204

    @admin_required
    def delete(self, nid: int):
        director_service.delete(nid)
        return "", 204
