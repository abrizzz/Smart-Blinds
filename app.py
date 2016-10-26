from flask import Flask, jsonify, request
from flask_restful import Api, Resource
import blinds
import sun

app = Flask(__name__)
api = Api(app)

b = blinds.Blinds()

class BlindsAPI(Resource):
    def __init__(self):
        super(BlindsAPI,self).__init__()

    def get(self):
        return jsonify({'opened': b.blinds_open})

    def post(self):
        b.toggle_blinds();
        return jsonify({'opened': b.blinds_open})

api.add_resource(BlindsAPI, '/blinds', endpoint='blinds')

class HelloWorld(Resource):
    def get(self):
        return 'Nothing to see here!'

api.add_resource(HelloWorld, '/')


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
