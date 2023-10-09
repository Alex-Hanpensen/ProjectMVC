from app.dao.user_dao import UserDAO


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.user_dao = user_dao

    def get_one(self, u_id):
        return self.user_dao.get_one(u_id)

    def get_all(self):
        return self.user_dao.get_all()

    def get_username(self, username):
        return self.user_dao.get_username(username)

    def create(self, data):
        data['password'] = self.generator_password(data['password'])
        return self.user_dao.create(data)

    def update(self, data):
        u_id = data.get('id')
        user = self.get_one(u_id)

        user.username = data.get("username")
        user.password = data.get("password")
        user.role = data.get("role")

        self.user_dao.update(user)

    def update_partial(self, data):
        u_id = data.get('id')
        user = self.get_one(u_id)

        if 'username' in data:
            user.username = data.get("username")
        if 'password' in data:
            user.password = data.get("password")
        if 'role' in data:
            user.role = data.get("role")

        self.user_dao.update(user)

    def delete(self, u_id):
        self.user_dao.delete(u_id)

    def generator_password(self, password):
        return self.user_dao.generator_password(password)

    def generator_tokens(self, username, password, is_refresh=False):
        pass

    def compare_password(self, password_hash, other_password):
        return self.user_dao.compare_password(password_hash, other_password)
