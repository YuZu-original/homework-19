from flask import request
from flask_restx import Resource, Namespace

from app.container import director_service
from app.dao.model.director import DirectorSchema
from app.decorators import auth_required, admin_required

director_ns = Namespace('directors')

director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

@director_ns.route('/')
class DirectorsView(Resource):
    @auth_required
    def get(self):
        directors = director_service.get_all()
        return directors_schema.dump(directors), 200
    
    @admin_required
    def post(self):
        data_json = request.json
        director = director_service.create(data_json)
        return "", 201, {"location": f"/directors/{director.id}"}


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    @auth_required
    def get(self, director_id):
        director = director_service.get_one(director_id)
        return director_schema.dump(director), 200
    
    @admin_required
    def put(self, director_id):
        data_json = request.json
        data_json["id"] = director_id
        director_service.update(data_json)
        return "", 204
    
    @admin_required
    def delete(self, director_id):
        director_service.delete(director_id)
        return "", 200