from flask import Flask
from flask_restful import request, reqparse, abort, Api, Resource
from gobang.data import Board,Move,MoveEncoder
import json

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('idCode', type=int)
parser.add_argument('boardSize', type=int)
parser.add_argument('playerData', type=dict)

# @app.route('/gobang/nextMove/',methods=['POST'])
# def fetch_next_move():


class Answer(Resource):
    def post(self):
        args = parser.parse_args()
        # args=request.json()
        board = Board(args['idCode'], args['boardSize'], args['playerData'])
        print(args['playerData'])
        move=Move(1,1)
        return move.display(), 200


api.add_resource(Answer, "/gobang/answer")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8697', debug=True)
