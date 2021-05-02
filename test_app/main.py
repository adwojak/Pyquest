from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
from test_app.resources import BasicResource, ArgumentsResource

app = Flask(__name__)
api = Api(app)
load_dotenv('.env')


api.add_resource(BasicResource, '/basic')
api.add_resource(ArgumentsResource, '/arguments')


if __name__ == '__main__':
    app.run(debug=True)
