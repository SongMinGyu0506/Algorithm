from pprint import pprint
import sys
from collections import deque

dx,dy = [0,0,1,-1],[1,-1,0,0]

def bfs(graph,y,x,visited,M,N):
    que = deque()
    visited[y][x] = False
    que.append([y,x])
    graph[y][x] = 0
    while que:
        cy,cx = que.popleft()
        for i in range(4):
            ny = cy+dy[i]
            nx = cx+dx[i]
            if (0 <= nx < M) and (0 <= ny < N) and (visited[ny][nx] == True) and (graph[ny][nx] == 1):
                visited[ny][nx] = False
                graph[ny][nx] = 0
                que.append([ny,nx])


T = int(sys.stdin.readline())
for i in range(T):
    cnt = 0
    M,N,K = map(int,sys.stdin.readline().split())
    data = [[0]*M for _ in range(N)]
    visited = [[True]*M for _ in range(N)]
    for i in range(K):
        X,Y = map(int,sys.stdin.readline().split())
        data[Y][X] = 1
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                bfs(data,i,j,visited,M,N)
                cnt += 1
    pprint(cnt)
