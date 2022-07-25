from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session
    
    def get_one(self, mid):
        return self.session.query(Movie).get(mid)
    
    def get_all(self, filters: dict):
        query = self.session.query(Movie)
        if filters.get("director_id"):
            query = query.filter(Movie.director_id == filters.get("director_id"))
        if filters.get("genre_id"):
            query = query.filter(Movie.genre_id == filters.get("genre_id"))
        if filters.get("year"):
            query = query.filter(Movie.year == filters.get("year"))
        
        return query.all()
    
    def create(self, data):
        movie = Movie(**data)
        self.session.add(movie)
        self.session.commit()
        return movie
    
    def update(self, data):
        movie = self.get_one(data.get("id"))
        
        movie.title = data.get("title")
        movie.description = data.get("description")
        movie.trailer = data.get("trailer")
        movie.year = data.get("year")
        movie.rating = data.get("rating")
        movie.genre_id = data.get("genre_id")
        movie.director_id = data.get("director_id")

        self.session.add(movie)
        self.session.commit()
    
    def delete(self, mid):
        movie = self.get_one(mid)
        
        self.session.delete(movie)
        self.session.commit()