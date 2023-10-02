from flask_restx import Resource, Namespace
from flask import request
from app.container import movie_service
from app.dao.model.movie_model import MovieSchema

movie_ns = Namespace('movies')
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        all_movies = movie_service.create(req_json)
        return "", 201


@movie_ns.route('/<int:u_id>')
class MovieView(Resource):
    def get(self, u_id):
        try:
            movie = movie_service.get_one(u_id)
            return movie_schema.dump(movie), 200
        except Exception as e:
            return "", 404

    def put(self, u_id):
        req_json = request.json
        req_json['id'] = u_id

        movie_service.update(req_json)
        return "", 204

    def path(self, u_id):
        req_json = request.json
        req_json['id'] = u_id

        movie_service.update_partial(req_json)
        return "", 204

    def delete(self, u_id: int):
        movie_service.delete(u_id)
        return "", 204
