from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from test_app.resources import ExampleResource, ArgumentsResource, JwtResource
from flask_jwt_extended import JWTManager


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secret"
api = Api(app)
jwt = JWTManager(app)
load_dotenv('.env')


api.add_resource(ExampleResource, '/example')
api.add_resource(ArgumentsResource, '/arguments')
api.add_resource(JwtResource, '/jwt')


if __name__ == '__main__':
    app.run(debug=True)
