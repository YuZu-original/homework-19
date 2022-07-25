from flask import request
from flask_restx import Resource, Namespace

from app.container import movie_service
from app.dao.model.movie import MovieSchema
from app.decorators import auth_required, admin_required

movie_ns = Namespace('movies')

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

@movie_ns.route('/')
class MoviesView(Resource):
    @auth_required
    def get(self):
        director_id = request.args.get("director_id", type=int)
        genre_id = request.args.get("genre_id", type=int)
        year = request.args.get("year", type=int)
        
        movies = movie_service.get_all(
            {
                "director_id":director_id,
                "genre_id": genre_id,
                "year": year,
            }
        )
        return movies_schema.dump(movies), 200
    
    @admin_required
    def post(self):
        data_json = request.json
        movie = movie_service.create(data_json)
        return "", 201, {"location": f"/movies/{movie.id}"}

@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    @auth_required
    def get(self, mid):
        movie = movie_service.get_one(mid)
        return movie_schema.dump(movie), 200
    
    @admin_required
    def put(self, mid):
        data_json = request.json
        data_json["id"] = mid
        movie_service.update(data_json)
        return "", 204
    
    @admin_required
    def delete(self, mid):
        movie_service.delete(mid)
        return "", 200