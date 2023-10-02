from flask_restx import Resource, Namespace
from app.container import genre_service
from app.dao.model.genre_model import GenreSchema

genre_ns = Namespace('genres')
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genrs = genre_service.get_all()
        return genres_schema.dump(all_genrs), 200


@genre_ns.route('/<int:u_id>')
class GenreView(Resource):
    def get(self, u_id):
        try:
            gener = genre_service.get_one(u_id)
            return genre_schema.dump(gener), 200
        except Exception as e:
            return "", 404
