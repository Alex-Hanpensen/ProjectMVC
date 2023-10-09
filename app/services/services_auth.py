from app.helpers.constants import JWT_SECRET, JWT_ALGORITHM
from app.services.services_user import UserService
from flask import abort
import datetime
import calendar
import jwt


class ServicesAuth:
    def __init__(self, user_services: UserService):
        self.user_services = user_services

    def generate_token(self, username, password, is_refresh=False):
        user = self.user_services.get_username(username)

        if user is None:
            raise abort(404)

        if not is_refresh:
            if not self.user_services.compare_password(user.password, password):
                abort(400)

        data = {
            'username': user.username,
            'role': user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, key=JWT_SECRET, algorithm=JWT_ALGORITHM)

        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, key=JWT_SECRET, algorithm=JWT_ALGORITHM)
        return {
            'access_token': access_token,
            'refresh_token': refresh_token
        }

    def approve_refresh_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username = data.get('username')
        return self.generate_token(username, None, is_refresh=True)
