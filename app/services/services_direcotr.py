from app.dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_one(self, d_id):
        return self.director_dao.get_one(d_id)

    def get_all(self):
        return self.director_dao.get_all()
