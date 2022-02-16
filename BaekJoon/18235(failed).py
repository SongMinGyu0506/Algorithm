from collections import deque


N,A,B = map(int,input().split())
five_visited = set()
six_visited = set()

def bfs(N,A,B):
    five_que = deque()
    six_que = deque()
    five_visited.add(A)
    six_visited.add(B)
    five_que.append([[A,1]])
    six_que.append([[B,1]])

    if five_que[0][0] == six_que[0][0] and five_que[0][1] == six_que[0][1]:
        return 1

    while (five_que and six_que):
        tmp_fives = []
        tmp_sixs = []
        fives = five_que.popleft()
        sixs = six_que.popleft()

        for five in fives:
            five_visited.add(five[0])
            next_five = five[0] + (2**(five[1]-1))
            prev_five = five[0] - (2**(five[1]-1))
            if next_five <= N and next_five not in five_visited:
                tmp_fives.append([next_five,five[1]+1])
            if prev_five > 0 and prev_five not in five_visited:
                tmp_fives.append([prev_five,five[1]+1])

        for six in sixs:
            six_visited.add(six[0])
            next_six = six[0] + (2**(six[1]-1))
            prev_six = six[0] - (2**(six[1]-1))
            if next_six <= N and next_six not in six_visited:
                tmp_sixs.append([next_six,six[1]+1])
            if prev_six > 0 and prev_six not in six_visited:
                tmp_sixs.append([prev_six,six[1]+1])
        
        try:
            five[0][0] -= 1
            five[0][0] += 1
            six[0][0] -= 1
            six[0][0] += 1
        except:
            return -1

        for six in tmp_sixs:
            for five in tmp_fives:
                if six[1] == five[1] and six[0] == five[0]:
                    return five[1]

        five_que.append(tmp_fives)
        six_que.append(tmp_sixs)
    return -1

print(bfs(N,A,B))