from unittest.mock import MagicMock
import pytest

from app.dao.model.movie_model import Movie
from app.dao.movie_dao import MovieDAO
from app.services.services_movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    d1 = Movie(id=1, title="Душа")
    d2 = Movie(id=2, title="Монстр в Париже")
    d3 = Movie(id=3, title="Упс... Приплыли!")

    movie_dao.get_one = MagicMock(return_value=d1)
    movie_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    movie_dao.create = MagicMock(return_value=Movie(id=3, title="Упс... Приплыли!"))
    movie_dao.delete = MagicMock(return_value=None)

    return movie_dao


class TestService:
    @pytest.fixture(autouse=True)
    def user_service(self, movie_dao):
        self.movie_service = MovieService(movie_dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_created(self):
        data = {
            "id": 3,
            "name": "Фэнтези",
        }
        movie = self.movie_service.create(data)
        assert movie.id is not None

    def test_delete(self):
        movie = self.movie_service.delete(1)
        assert movie is None
