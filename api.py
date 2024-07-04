from flask import Flask, jsonify, request 
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
parser.add_argument('id', type=int)

result={
    'id_1' : 1088,
    'id_2' : 1093,
    'id_3' : 1097
}

class model_knn(Resource):
    def get(self, id):
        print('get: ', id)
        return jsonify({'data': result})

    def post(self, id):
        args = parser.parse_args()
        print('post: ',args)
        return jsonify({'data': result})

api.add_resource(model_knn, '/model_knn/<int:id>')

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8000)