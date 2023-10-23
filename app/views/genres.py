from flask import request
from app.container import genre_service
from flask_restx import Resource, Namespace
from app.dao.model.genre_model import GenreSchema
from app.helpers.decortors import auth_required, admin_required

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):

    def get(self):
        page = request.args.get('page', None, type=int)
        if page:
            all_genrs = genre_service.get_page(page)
        else:
            all_genrs = genre_service.get_all()
        return genres_schema.dump(all_genrs), 200

    @admin_required
    def post(self):
        req_json = request.json
        all_genres = genre_service.create(req_json)
        return "", 201


@genre_ns.route('/<int:g_id>')
class GenreView(Resource):
    @auth_required
    def get(self, g_id):
        try:
            gener = genre_service.get_one(g_id)
            return genre_schema.dump(gener), 200
        except Exception as e:
            return "", 404

    @admin_required
    def put(self, g_id):
        req_json = request.json
        req_json['id'] = g_id

        genre_service.update(req_json)
        return "", 204

    def patch(self, g_id):
        req_json = request.json
        req_json['id'] = g_id

        genre_service.update_partial(req_json)
        return "", 204

    @admin_required
    def delete(self, g_id):
        genre_service.delete(g_id)
        return "", 204
