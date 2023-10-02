from app.dao.model.movie_model import Movie


#  CRUD
class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, m_id):
        return self.session.query(Movie).get(m_id)

    def get_all(self):
        return self.session.query(Movie).all()

    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()

    def update(self, movie):
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, m_id):
        movie = self.get_one(m_id)
        self.session.delete(movie)
        self.session.commit()
