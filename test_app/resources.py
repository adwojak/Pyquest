from flask_restful import Resource, request


class BasicResource(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'world': 'hello'}


class ArgumentsResource(Resource):

    def post(self):
        return request.form

    def put(self):
        return request.form
