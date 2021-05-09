from datetime import timedelta
from flask_restful import Resource, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required


class ExampleResource(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'world': 'hello'}


class ArgumentsResource(Resource):

    @jwt_required()
    def get(self):
        return {'status': 'Authorized!'}

    def post(self):
        return request.form

    def put(self):
        return request.form


class JwtResource(Resource):
    expires_in = timedelta(seconds=1)

    def post(self):
        form = request.form
        if 'refresh_token' in form:
            return {
                'access_token': create_access_token(identity='example@email.com', expires_delta=self.expires_in),
                'refresh_token': create_refresh_token(identity='example@email.com', expires_delta=self.expires_in),
                'expires_in': self.expires_in.seconds,
                'from_refresh': True
            }
        return {
            'access_token': create_access_token(identity='example@email.com', expires_delta=self.expires_in),
            'refresh_token': create_refresh_token(identity='example@email.com', expires_delta=self.expires_in),
            'expires_in': self.expires_in.seconds,
        }
