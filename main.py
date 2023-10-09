from flask import Flask
from flask_restx import Api
from app.config import Config
from app.dao.model.director_model import Director
from app.dao.model.genre_model import Genre
from app.dao.model.movie_model import Movie
from app.dao.model.user_model import User
from app.setup_db import db
from app.create_data import movies_data, directors_data, genres_data
from app.views.auth import auth_ns
from app.views.directors import director_ns
from app.views.genres import genre_ns
from app.views.movies import movie_ns
from app.views.users import user_ns


def create_app(config: Config):
    application = Flask(__name__)
    application.config.from_object(config)
    application.app_context().push()
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(director_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)
    create_data(application, db)


def create_data(app, db):
    with app.app_context():
        db.create_all()
        u1 = User(username="vasya", password="my_little_pony", role="user")
        u2 = User(username="oleg", password="qwerty", role="user")
        u3 = User(username="oleg", password="P@ssw0rd", role="admin")

        with db.session.begin():
            for movie in movies_data:
                result = Movie(**movie)
                db.session.add(result)
            for director in directors_data:
                result = Director(**director)
                db.session.add(result)
            for genre in genres_data:
                result = Genre(**genre)
                db.session.add(result)

            db.session.add_all([u1, u2, u3])
            db.session.commit()


if __name__ == '__main__':
    app = create_app(Config())
    register_extensions(app)
    app.run()
