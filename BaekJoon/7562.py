from collections import deque


n = int(input())
for i in range(n):
    length = int(input())
    board = [[0]*length for i in range(length+1)]
    visited = [[False]*length for i in range(length+1)]
    sy,sx = map(int,input().split())
    ty,tx = map(int,input().split())

    que = deque()

    board[sy][sx] = 1
    
    que.append([sy,sx,0])
    
    dy = [2,1,    -1,-2,   -1,-2,   1,2]
    dx = [1,2,     2,1,     -2,-1,  -2,-1]
    while que:
        cy,cx,cnt = que.popleft()
        if visited[cy][cx] == True:
            continue
        if cy == ty and cx == tx:
            print(cnt)
            break
        visited[cy][cx] = True
        for i in range(len(dy)):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if (0 <= ny < length) and (0 <= nx < length):
                if not visited[ny][nx]:
                    que.append([ny,nx,cnt+1])
