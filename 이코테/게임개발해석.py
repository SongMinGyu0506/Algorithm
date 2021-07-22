n,m = map(int,input().split())
d = [[0]*m for _ in range(n)]
x,y,direction = map(int,input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1 #최종 카운트
turn_time = 0 #회전 횟수
while True:
    turn_left() #일단 왼쪽으로 회전
    nx = x + dx[direction] #이동 예정 좌표
    ny = y + dy[direction]

    #체크 좌표 또는 이동 가능할때
    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:
        turn_time += 1 #회전 했다는 것만 추가
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0:
            x = nx
            y = ny
        else :
            break
        turn_time = 0

print(count)