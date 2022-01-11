graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visitied = [False] * 9

def dfs(graph,start,visited):
    visited[start] = True
    print(start,end=" ")
    for i in graph[start]:
        if not visitied[i]:
            dfs(graph,i,visitied)

dfs(graph,1,visitied)
print()
from collections import deque
visitied = [False] * 9

def bfs(graph,v,visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        n = queue.popleft()
        print(n,end=' ')
        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

bfs(graph,1,visitied)