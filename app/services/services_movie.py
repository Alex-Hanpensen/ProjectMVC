from app.dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_one(self, m_id):
        return self.movie_dao.get_one(m_id)

    def get_new_movies(self):
        return self.movie_dao.get_new_movies()

    def get_page(self, page):
        return self.movie_dao.get_page(page)

    def get_all(self):
        return self.movie_dao.get_all()

    def create(self, data):
        return self.movie_dao.create(data)

    def update(self, data):
        m_id = data.get('id')
        movie = self.get_one(m_id)

        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.genre = data.get("genre")
        movie.director_id = data.get("director_id")
        movie.director = data.get("director")

        self.movie_dao.update(movie)

    def update_partial(self, data):
        m_id = data.get('id')
        movie = self.get_one(m_id)

        if 'title' in data:
            movie.title = data.get("title")
        if 'description' in data:
            movie.description = data.get("description")
        if 'trailer' in data:
            movie.trailer = data.get("trailer")
        if 'year' in data:
            movie.year = data.get("year")
        if 'rating' in data:
            movie.rating = data.get("rating")
        if 'genre_id' in data:
            movie.genre_id = data.get("genre_id")
        if 'genre' in data:
            movie.genre = data.get("genre")
        if 'director_id' in data:
            movie.director_id = data.get("director_id")
        if 'director' in data:
            movie.director = data.get("director")

        self.movie_dao.update(movie)

    def delete(self, m_id):
        self.movie_dao.delete(m_id)
