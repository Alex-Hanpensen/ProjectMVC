from app.dao.user_dao import UserDAO


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_one(self, u_id):
        return self.user_dao.get_one(u_id)

    def get_all(self):
        return self.user_dao.get_all()

    def get_username(self, name):
        return self.user_dao.get_username(name)

    def get_email(self, email):
        return self.user_dao.get_email(email)

    def create(self, data):
        data['password'] = self.generator_password(data['password'])
        return self.user_dao.create(data)

    def update(self, data):
        u_id = data.get('id')
        user = self.get_one(u_id)

        user.name = data.get("name")
        user.surname = data.get("surname")
        user.favorite_genre = data.get("favorite_genre")

        self.user_dao.update(user)

    def update_partial(self, data):
        u_id = data.get('id')
        user = self.get_one(u_id)

        if 'password_1' in data and self.user_dao.compare_password(user.password, data.get('password_1')):
            data['password'] = self.generator_password(data['password_2'])
            user.password = data['password']
            self.user_dao.update(user)

    def delete(self, u_id):
        self.user_dao.delete(u_id)

    def generator_password(self, password):
        return self.user_dao.generator_password(password)

    def compare_password(self, password_hash, other_password):
        return self.user_dao.compare_password(password_hash, other_password)
