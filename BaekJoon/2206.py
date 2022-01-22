from collections import deque
import pprint
N,M = map(int,input().split(' '))
array = [list(map(int, input())) for _ in range(N)]
visited1 = [[float("inf") for _ in range(M)] for _ in range(N)]
visited2 = [[float("inf") for _ in range(M)] for _ in range(N)]

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(array,x,y,wall_counter,visited,visited_counter):
    que = deque([(y,x,wall_counter,visited_counter)])
    visited[y][x] = visited_counter

    while que:
        y,x,wall_counter,visited_counter = que.popleft()
        visited_counter += 1
        
        for i in range(4):
            ay = y + dy[i]
            ax = x + dx[i]
            if (ax >= 0 and ax < M) and (ay >= 0 and ay < N):
                if array[ay][ax] == 1 and wall_counter == True:
                    visited[ay][ax] = visited_counter
                    que.append((ay,ax,False,visited_counter))

                elif array[ay][ax] == 0 and visited[ay][ax] == float('inf'):
                    que.append((ay,ax,wall_counter,visited_counter))
                    visited[ay][ax] = visited_counter

bfs(array,0,0,True,visited1,1)
bfs(array,0,0,False,visited2,1)

pprint.pprint(visited1)
print()
pprint.pprint(visited2)

results = min(visited2[N-1][M-1],visited1[N-1][M-1])
if results == float('inf'):
    print(-1)
else:
    print(results)

