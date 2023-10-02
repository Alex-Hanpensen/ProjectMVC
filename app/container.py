from app.dao.director_dao import DirectorDAO
from app.dao.genre_dao import GenreDAO
from app.dao.movie_dao import MovieDAO

from app.services.services_direcotr import DirectorService
from app.services.services_genre import GenreService
from app.services.services_movie import MovieService

from app.setup_db import db

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
