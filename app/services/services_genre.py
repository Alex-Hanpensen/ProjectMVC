from app.dao.genre_dao import GenreDAO


class GenreService:
    def __init__(self, director_dao: GenreDAO):
        self.director_dao = director_dao

    def get_one(self, d_id):
        return self.director_dao.get_one(d_id)

    def get_all(self):
        return self.director_dao.get_all()
