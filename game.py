from flask import Flask,request
from flask_restful import reqparse, abort, Api, Resource
from gobang.data import Board,Move,MoveEncoder
import json
import http_util

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
        # args=request.json()
        print(request.form.get("playerData"))
        board = Board(request.form.get('idCode'), request.form.get('boardSize'), request.form.get('playerData'))
        move=Move(1,1)
        return http_util.buildSuccess(move.display()),200

api.add_resource(Answer, "/gobang/answer")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8697', debug=True)
