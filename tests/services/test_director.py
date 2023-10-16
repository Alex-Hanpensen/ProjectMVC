from unittest.mock import MagicMock
import pytest

from app.dao.director_dao import DirectorDAO
from app.dao.model.director_model import Director
from app.services.services_director import DirectorService


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(None)

    d1 = Director(id=1, name="Тейлор Шеридан")
    d2 = Director(id=2, name="Квентин Тарантино")
    d3 = Director(id=3, name="Владимир Вайншток")

    director_dao.get_one = MagicMock(return_value=d1)
    director_dao.get_all = MagicMock(return_value=[d1, d2, d3])
    director_dao.create = MagicMock(return_value=Director(id=3, name="Владимир Вайншток"))
    director_dao.delete = MagicMock(return_value=None)

    return director_dao


class TestService:
    @pytest.fixture(autouse=True)
    def user_service(self, director_dao):
        self.director_service = DirectorService(director_dao=director_dao)

    def test_get_one(self):
        director = self.director_service.get_one(1)
        assert director is not None
        assert director.id is not None

    def test_get_all(self):
        directors = self.director_service.get_all()
        assert len(directors) > 0

    def test_created(self):
        data = {
            "id": 3,
            "name": "Владимир Вайншток",
        }
        director = self.director_service.create(data)
        assert director.id is not None

    def test_delete(self):
        director = self.director_service.delete(1)
        assert director is None
