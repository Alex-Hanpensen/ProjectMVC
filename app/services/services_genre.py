from app.dao.genre_dao import GenreDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_one(self, g_id):
        return self.genre_dao.get_one(g_id)

    def get_all(self):
        return self.genre_dao.get_all()

    def create(self, data):
        return self.genre_dao.create(data)

    def update(self, data):
        g_id = data.get('id')
        genre = self.get_one(g_id)

        genre.name = data.get("name")

        self.genre_dao.update(genre)

    def update_partial(self, data):
        d_id = data.get('id')
        genre = self.get_one(d_id)

        if 'name' in data:
            genre.name = data.get("name")

        self.genre_dao.update(genre)

    def delete(self, g_id):
        self.genre_dao.delete(g_id)
