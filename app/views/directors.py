from flask_restx import Resource, Namespace
from app.container import director_service
from app.dao.model.director_model import DirectorsSchema

director_ns = Namespace('directors')
director_schema = DirectorsSchema()
directors_schema = DirectorsSchema(many=True)


@director_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        all_directors = director_service.get_all()
        return directors_schema.dump(all_directors), 200


@director_ns.route('/<int:u_id>')
class DirectorView(Resource):
    def get(self, u_id):
        try:
            director = director_service.get_one(u_id)
            return director_schema.dump(director), 200
        except Exception as e:
            return "", 404
