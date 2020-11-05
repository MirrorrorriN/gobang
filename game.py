import score
class Board(object):
    def __init__(self, steps={"1": [], "2": []}, side=1, scale=15):
        self.steps = steps
        self.side = side
        self.scale = scale
        self.mesh = [[0 for col in range(scale)] for row in range(scale)]
        self.score = [[0 for col in range(scale)] for row in range(scale)]
        black_steps = steps["1"]
        white_steps = steps["2"]
        for i in range(len(black_steps)):
            self.mesh[black_steps[i][0]][black_steps[i][1]] = 1
        for i in range(len(white_steps)):
            self.mesh[white_steps[i][0]][white_steps[i][1]] = 2
        #评分表初始化待优化
        for i in range(scale):
            for j in range(scale):
                black_count=0
                white_count=0
                for k in range(max(0,i-4),min(i+4,scale-1)):
                    if(mesh[k][j]!=0):
                        score[k][j]=-1
                        continue
                    

        print("******init*******")

    def scan_steps(self, steps, side, scale):
        if (side != self.side or scale != self.scale):
            # 重新初始化
            return Board(steps, side, scale)
        black_steps = steps["1"]
        white_steps = steps["2"]
        if(len(black_steps)-len(self.steps["1"]) < 0 or len(white_steps)-len(self.steps["2"]) < 0):
            return Board(steps, side,scale)
        cur_black_steps = self.steps["1"]
        cur_white_steps = self.steps["2"]
        for i in range(len(cur_black_steps)):
            if(black_steps[i][0] != cur_black_steps[i][0] or black_steps[i][1] != cur_black_steps[i][1]):
                return Board(steps, side,scale)
        for i in range(len(cur_white_steps)):
            if(white_steps[i][0] != cur_white_steps[i][0] or white_steps[i][1] != cur_white_steps[i][1]):
                return Board(steps, side,scale)
        
        self.steps=steps
        for i in range(len(cur_black_steps),len(black_steps)):
            self.mesh[black_steps[i][0]][black_steps[i][1]] = 1
        for i in range(len(cur_white_steps),len(white_steps)):
            self.mesh[white_steps[i][0]][white_steps[i][1]] = 2
        return self

    def display_mesh(self):
        for i in range(len(self.mesh)):
            print (self.mesh[i])


