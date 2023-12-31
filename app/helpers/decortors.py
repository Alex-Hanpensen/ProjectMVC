import jwt
from flask import request, abort
from app.helpers.constants import JWT_SECRET, JWT_ALGORITHM


def auth_required(func):
    """
    Checks registration
    :param func:
    :return: func
    """
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as e:
            print(f"Traceback: {e}")
            abort(401)
        return func(*args, **kwargs)

    return wrapper


def admin_required(func):
    """
       Checks registration and user privilege
       :param func:
       :return: func
       """
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)
        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        role = None
        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            role = user.get('role', 'user')
        except Exception as e:
            print(f"Traceback: {e}")
            abort(401)
        if role != 'admin':
            abort(403)

        return func(*args, **kwargs)

    return wrapper
