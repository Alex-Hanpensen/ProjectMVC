from app.dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_one(self, d_id):
        return self.director_dao.get_one(d_id)

    def get_all(self):
        return self.director_dao.get_all()

    def create(self, data):
        return self.director_dao.create(data)

    def update(self, data):
        d_id = data.get('id')
        director = self.get_one(d_id)

        director.name = data.get("name")

        self.director_dao.update(director)

    def update_partial(self, data):
        d_id = data.get('id')
        director = self.get_one(d_id)

        if 'name' in data:
            director.name = data.get("name")

        self.director_dao.update(director)

    def delete(self, d_id):
        self.director_dao.delete(d_id)
