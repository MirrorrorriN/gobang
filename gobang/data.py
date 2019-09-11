import json
# class Scene:
#     def __init__(self, idCode, boardSize, playerData):
#         self.idCode = idCode
#         self.boardSize = boardSize
#         self.playerData = playerData

#     def __str__(self):
#         return '[idCode] '+self.idCode+'[boardSize] '+self.boardSize+'[playerData] '+str(self.playerData)

class Move:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        res={}
        res['x']=self.x
        res['y']=self.y
        return res
    def display(self):
        res={}
        res['x']=self.x
        res['y']=self.y
        return res

class MoveEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,Move):
            return obj.__str__()
        return json.JSONEncoder.default(self,obj)

