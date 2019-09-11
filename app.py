from flask import Flask, request
from flask_restful import reqparse, abort, Api, Resource
from gobang.data import Move, MoveEncoder
import json
import http_util
import game
import traceback
import ast

app = Flask(__name__)
api = Api(app)

# @app.route('/gobang/nextMove/',methods=['POST'])
# def fetch_next_move():

board=game.Board()
x=1

class Answer(Resource):
    def post(self):
        try:
            # board = Scene(request.form.get('idCode'), request.form.get(
            #     'boardSize'), request.form.get('playerData'))
            global x
            global board
            #注意字符串到字典的转换
            playerDataDict=ast.literal_eval(request.form.get('playerData'))
            board=board.scan_steps(playerDataDict,request.form.get('idCode',type=int),request.form.get('boardSize',type=int))
            print (board.display_mesh())
            move = Move(x, x)
            x+=1
            return http_util.buildSuccess(move.display()), 200
        except Exception as e:
            print (traceback.print_exc())
            return http_util.buildFail(e)


api.add_resource(Answer, "/gobang/answer")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8697', debug=True)
