from flask_restful import Resource


class BasicResource(Resource):

    def get(self):
        return {'hello': 'world'}

    def post(self):
        return {'world': 'hello'}
