def solution(land):
    answer = 0
    m = len(land)
    score = [[0]*4 for i in range(m)]
    for y in range(1,m):
        for x in range(4):
            if x == 0:
                land[y][x] = max(land[y-1][1]+land[y][x],
                                 land[y-1][2]+land[y][x],
                                 land[y-1][3]+land[y][x])
            elif x == 1:
                land[y][x] = max(land[y-1][0]+land[y][x],
                                 land[y-1][2]+land[y][x],
                                 land[y-1][3]+land[y][x])
            elif x == 2:
                land[y][x] = max(land[y-1][0]+land[y][x],
                                 land[y-1][1]+land[y][x],
                                 land[y-1][3]+land[y][x])
            else:
                land[y][x] = max(land[y-1][0]+land[y][x],
                                 land[y-1][1]+land[y][x],
                                 land[y-1][2]+land[y][x])
    answer = max(land[len(land)-1])
    return answer