result = []
count = 0
n = int(input())
graph = []
visited = [[0]*n]*n
for _ in range(n):
    x = list(map(int,input()))
    graph.append(x)

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n or graph[x][y] == 0:
        return
    global count
    graph[x][y] = 0
    visited[x][y] = 1
    count += 1
    
    dfs(x-1,y)
    dfs(x+1,y)
    dfs(x,y-1)
    dfs(x,y+1)

for i in range(n):
    for j in range(n):
        if visited[i][j] != 1 and graph[i][j] == 1:
            dfs(i,j)
            result.append(count)
            count = 0

print(len(result))
for i in sorted(result):
    print(i)
