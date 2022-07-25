from flask import request
from flask_restx import Resource, Namespace

from app.dao.model.user import UserSchema
from app.container import user_service

user_ns = Namespace('users')

user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_ns.route('/')
class UsersView(Resource):
    def get(self):
        all_users = user_service.get_all()
        return users_schema.dump(all_users), 200

    def post(self):
        data = request.json
        user = user_service.create(data)
        return "", 201, {"location": f"/users/{user.id}"}


@user_ns.route('/<int:uid>')
class UserView(Resource):
    def get(self, uid):
        user = user_service.get_one(uid)
        return user_schema.dump(user), 200

    def put(self, uid):
        data = request.json
        
        if data.get("id") == None:
            data["id"] = uid

        user_service.update(data)
        return "", 204

    def delete(self, uid):
        user_service.delete(uid)
        return "", 204