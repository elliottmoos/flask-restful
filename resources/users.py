from flask import jsonify, Blueprint, abort, make_response
from flask_restful import (Resource, Api,
                        reqparse, inputs, fields,
                        marshal, marshal_with, url_for)
import models, json
from auth import auth

user_fields = {
    'username': fields.String
}

class UserList(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='No username provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'email',
            required=True,
            help='No email provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'password',
            required=True,
            help='No password provided',
            location=['form', 'json']
        )
        self.reqparse.add_argument(
            'verify_password',
            required=True,
            help='No password verification provided',
            location=['form', 'json']
        )
        super().__init__()
        
    def get(self):
        return jsonify({'users': [{'username': "elliottmoos"}]})

    @marshal_with
    def post(self):
        args = self.reqparse.parse_args()
        if args.get('password') == args.get('verify_password'):
            user = models.User.create_user(**args)
            return user, 201
        return make_response(json.dumps({'error': 'Password and password verification do not match.'}), 400)
    
class User(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'username',
            required=True,
            help='No username provided',
            location=['form', 'json'],
            type=str
        )
        self.reqparse.add_argument(
            'email',
            required=True,
            help='No email provided',
            location=['form', 'json'],
            type=str
        )
        super().__init__()
        
    def get(self, id):
        return jsonify({'username': 'elliottmoos'})

users_api = Blueprint('resources.users', __name__)
api = Api(users_api)
api.add_resource(
    UserList,
    '/users',
    endpoint='users'
)
api.add_resource(
    User,
    '/users/<int:id>',
    endpoint='user'
)