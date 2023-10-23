from app.dao.model.genre_model import Genre


#  CRUD
class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, g_id):
        return self.session.query(Genre).get(g_id)

    def get_page(self, page):
        return Genre.query.paginate(page=page, per_page=12)

    def get_all(self):
        return self.session.query(Genre).all()

    def create(self, data):
        genre = Genre(**data)
        self.session.add(genre)
        self.session.commit()

    def update(self, genre):
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, g_id):
        genre = self.get_one(g_id)
        self.session.delete(genre)
        self.session.commit()
