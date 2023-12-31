from flask_restx import Resource, Namespace
from flask import request
from app.container import auth_service

auth_ns = Namespace('auth')


@auth_ns.route('/login')
class AuthsView(Resource):
    def post(self):
        data = request.json

        email = data.get('email', None)
        password = data.get('password', None)

        if None in (email, password):
            return '', 400

        tokens = auth_service.generate_token(email, password)

        return tokens, 201

    def put(self):
        data = request.json

        refresh_token = data.get('refresh_token')
        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201


@auth_ns.route('/register/')
class AuthView(Resource):
    def post(self):
        data = request.json
        auth_service.user_services.create(data)
