from flask_restx import Resource, Namespace
from flask import request
from app.container import user_service
from app.dao.model.user_model import UserSchema
from app.helpers.decortors import admin_required

user_ns = Namespace('users')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self):
        req_json = request.json
        user_service.create(req_json)
        return "", 201


@user_ns.route('/<int:u_id>')
class MovieView(Resource):
    def get(self, u_id):
        try:
            user = user_service.get_one(u_id)
            return user_schema.dump(user), 200
        except Exception as e:
            return "", 404

    def put(self, u_id):
        req_json = request.json
        req_json['id'] = u_id

        user_service.update(req_json)
        return "", 204

    def path(self, u_id):
        req_json = request.json
        req_json['id'] = u_id

        user_service.update_partial(req_json)
        return "", 204

    @admin_required
    def delete(self, u_id: int):
        user_service.delete(u_id)
        return "", 204
