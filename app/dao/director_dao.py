from app.dao.model.director_model import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, d_id):
        return self.session.query(Director).get(d_id)

    def get_all(self):
        return self.session.query(Director).all()
