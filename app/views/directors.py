from flask import request
from app.container import director_service
from flask_restx import Resource, Namespace
from app.dao.model.director_model import DirectorsSchema
from app.helpers.decortors import auth_required, admin_required

director_ns = Namespace('directors')
director_schema = DirectorsSchema()
directors_schema = DirectorsSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):

    def get(self):
        page = request.args.get('page', None, type=int)
        if page:
            all_directors = director_service.get_page(page)
        else:
            all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200

    @admin_required
    def post(self):
        req_json = request.json
        all_directors = director_service.create(req_json)
        return "", 201


@director_ns.route('/<int:d_id>')
class DirectorView(Resource):
    @auth_required
    def get(self, d_id):
        try:
            director = director_service.get_one(d_id)
            return director_schema.dump(director), 200
        except Exception as e:
            return "", 404

    @admin_required
    def put(self, d_id):
        req_json = request.json
        req_json['id'] = d_id

        director_service.update(req_json)
        return "", 204

    def patch(self, d_id):
        req_json = request.json
        req_json['id'] = d_id

        director_service.update_partial(req_json)
        return "", 204

    @admin_required
    def delete(self, d_id):
        director_service.delete(d_id)
        return "", 204
