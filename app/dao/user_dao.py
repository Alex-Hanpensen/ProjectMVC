from app.dao.model.user_model import User
import base64
import hashlib
import hmac
from app.helpers.constants import PWD_HASH_ITERATIONS, PWD_HASH_SALT, JWT_ALGORITHM


#  CRUD
class UserDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, u_id):
        return self.session.query(User).get(u_id)

    def get_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    def get_all(self):
        return self.session.query(User).all()

    def create(self, data):
        user = User(**data)
        self.session.add(user)
        self.session.commit()

    def update(self, user):
        self.session.add(user)
        self.session.commit()
        return user

    def delete(self, u_id):
        movie = self.get_one(u_id)
        self.session.delete(movie)
        self.session.commit()

    def generator_password(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'SHA256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_password(self, password_hash, other_password):
        hash_password = hashlib.pbkdf2_hmac(
            'SHA256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(base64.b64decode(password_hash), hash_password)
