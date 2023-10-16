from unittest.mock import MagicMock
import pytest

from app.dao.genre_dao import GenreDAO
from app.dao.model.genre_model import Genre
from app.services.services_genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    d1 = Genre(id=1, name="Комедия")
    d2 = Genre(id=2, name="Семейный")
    d3 = Genre(id=3, name="Фэнтези")

    genre_dao.get_one = MagicMock(return_value=d1)
    genre_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    genre_dao.create = MagicMock(return_value=Genre(id=3, name="Фэнтези"))
    genre_dao.delete = MagicMock(return_value=None)

    return genre_dao


class TestService:
    @pytest.fixture(autouse=True)
    def user_service(self, genre_dao):
        self.genre_service = GenreService(genre_dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genre = self.genre_service.get_all()
        assert len(genre) > 0

    def test_created(self):
        data = {
            "id": 3,
            "name": "Фэнтези",
        }
        genre = self.genre_service.create(data)
        assert genre.id is not None

    def test_delete(self):
        genre = self.genre_service.delete(1)
        assert genre is None
