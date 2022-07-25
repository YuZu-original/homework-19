from flask import request
from flask_restx import Resource, Namespace

from app.container import genre_service
from app.dao.model.genre import GenreSchema
from app.decorators import auth_required, admin_required

genre_ns = Namespace('genres')

genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

@genre_ns.route('/')
class GenresView(Resource):
    @auth_required
    def get(self):
        genres = genre_service.get_all()
        return genres_schema.dump(genres), 200
    
    @admin_required
    def post(self):
        data_json = request.json
        genre = genre_service.create(data_json)
        return "", 201, {"location": f"/genres/{genre.id}"}


@genre_ns.route('/<int:genre_id>')
class GenreView(Resource):
    @auth_required
    def get(self, genre_id):
        genre = genre_service.get_one(genre_id)
        return genre_schema.dump(genre), 200
    
    @admin_required
    def put(self, genre_id):
        data_json = request.json
        data_json["id"] = genre_id
        genre_service.update(data_json)
        return "", 204
    
    @admin_required
    def delete(self, genre_id):
        genre_service.delete(genre_id)
        return "", 200