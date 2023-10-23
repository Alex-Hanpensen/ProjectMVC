from unittest.mock import MagicMock
import pytest
from flask_restx import Namespace

from app.dao.model.user_model import User
from app.dao.user_dao import UserDAO
from app.services.services_user import UserService

user_ns = Namespace('users')


@pytest.fixture()
def user_dao():
    user_dao = UserDAO(None)

    user_dao.get_all = MagicMock(return_value=[User(password='qwerty', email='email90.ru')])
    user_dao.create = MagicMock(return_value='"", 201')
    user_dao.delete = MagicMock(return_value=None)

    return user_dao


@user_ns.route('/')
class TestUserViews:
    @pytest.fixture(autouse=True)
    def user_service(self, user_dao):
        self.user_dao = UserService(user_dao=user_dao)

    def test_get_all(self):
        assert len(self.user_dao.get_all()) > 0

    def test_create(self):
        data = {'password': 'qwerty', 'email': 'email90.ru'}
        assert self.user_dao.create(data) == '"", 201'

    def test_delete(self):
        assert self.user_dao.delete(1) is None
