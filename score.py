# black_score = [7, 25, 800, 15000, 800000, 15, 400, 1800, 100000, 0, 0]
# white_score = [7, 15, 400, 1800, 100000, 25, 800, 15000, 800000, 0, 0]
blank_score = 7
own_score_list = [25, 800, 15000, 800000]
opp_score_list = [15, 400, 1800, 100000]
polluted_score = 0
invalid_score = 0

# black_score = [7, 35, 800, 15000, 800000, 20, 500, 4000, 300000, 0, 0]
# white_score = [7, 20, 500, 4000, 300000, 35, 800, 15000, 800000, 0, 0]

# 计算某一个落点的得分


def get_point_score(x, y, scale, mesh, side):
    if(mesh[x][y] != 0):
        return -1
    score = 0

    # 水平方向扫描
    quintet_count = [0, 0]
    for i in range(max(0, i-4), min(i, scale-1-4)):
        if(i == max(0, i-4)):
            for j in range(5):
                quintet_count[mesh[i+j][y]-1] += 1
        else:
            quintet_count[mesh[i-1][y]-1] -= 1
            quintet_count[mehs[i+4][y]-1] += 1
        if(quintet_count[0] == 0 | quintet_count[1] == 0):
            score += blank_score
            continue
        if(quintet_count[0]*quintet_count[1] == 0):
            score += 0
            continue
        if(quintet_count[side-1] > 0):
            score += own_score_list[quintet_count[side-1]-1]
            continue
        if(quintet_count[2-side] > 0):
            score += opp_score_list[quintet_count[2-side]-1]
            continue
    
    # 竖直方向扫描
    quintet_count = [0, 0]
    for i in range(max(0, i-4), min(i, scale-1-4)):
        if(i == max(0, i-4)):
            for j in range(5):
                quintet_count[mesh[x][i+j]-1] += 1
        else:
            quintet_count[mesh[x][i-1]-1] -= 1
            quintet_count[mehs[x][i+4]-1] += 1
        if(quintet_count[0] == 0 | quintet_count[1] == 0):
            score += blank_score
            continue
        if(quintet_count[0]*quintet_count[1] == 0):
            score += 0
            continue
        if(quintet_count[side-1] > 0):
            score += own_score_list[quintet_count[side-1]-1]
            continue
        if(quintet_count[2-side] > 0):
            score += opp_score_list[quintet_count[2-side]-1]
            continue

    # 对角线方向扫描
    quintet_count = [0, 0]
    for i in range(-4,4):
        if(i == max(0, i-4)):
            for j in range(5):
                quintet_count[mesh[i+j][y]-1] += 1
        else:
            quintet_count[mesh[i-1][y]-1] -= 1
            quintet_count[mehs[i+4][y]-1] += 1
        if(quintet_count[0] == 0 | quintet_count[1] == 0):
            score += blank_score
            continue
        if(quintet_count[0]*quintet_count[1] == 0):
            score += 0
            continue
        if(quintet_count[side-1] > 0):
            score += own_score_list[quintet_count[side-1]-1]
            continue
        if(quintet_count[2-side] > 0):
            score += opp_score_list[quintet_count[2-side]-1]
            continue

    # 反对角线方向扫描
    quintet_count = [0, 0]
    for i in range(max(0, i-4), min(i, scale-1-4)):
        if(i == max(0, i-4)):
            for j in range(5):
                quintet_count[mesh[i+j][y]-1] += 1
        else:
            quintet_count[mesh[i-1][y]-1] -= 1
            quintet_count[mehs[i+4][y]-1] += 1
        if(quintet_count[0] == 0 | quintet_count[1] == 0):
            score += blank_score
            continue
        if(quintet_count[0]*quintet_count[1] == 0):
            score += 0
            continue
        if(quintet_count[side-1] > 0):
            score += own_score_list[quintet_count[side-1]-1]
            continue
        if(quintet_count[2-side] > 0):
            score += opp_score_list[quintet_count[2-side]-1]
            continue
    
    return score
