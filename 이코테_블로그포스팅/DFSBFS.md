# 📖 DFS & BFS

## 📌 서론
그래프의 완전탐색 기법중 하나, 코딩 테스트 문제에서 보통 길찾기 또는 영역 구분 등 입력 값이 보통 2차원으로 입력받는다면, DFS 또는 BFS로 해결이 가능한 문제들이 종종 있다. 또한 해당 개념을 기반으로 추가적인 풀이를 요구할 수 있다. 그렇기 때문에 가장 기본이되는 DFS/BFS를 정리한다.

## 📌 특징
* 기본적으로 DFS/BFS 모두 그래프의 모든 정점을 거친다는 점은 같다.
* 한번 거친 정점은 다시 거쳐가지 않는다.
* DFS는 깊이 우선 탐색 (Depth-Fist Search)으로, 정점과 연결된 정점을 탐색하고 이동할 때, 한 지점만 우선적으로 탐색한다. 즉, Stack의 방식을 이용하여 정점을 탐색한다.
* BFS는 너비 우선 탐색 (Breadth-First Search)으로, 정점과 연결된 정점을 탐색하고 이동할 때, 연결된 모든 정점을 탐색하는 방식으로 탐색을 진행한다. 따라서 BFS는 Queue를 이용한다.
* 일반적으로 DFS가 구현난이도는 조금 더 쉽다.

## 📌 구현
### __testcase__
```python
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

visited = [False] * 9
```
테스트 케이스로는 이중 리스트를 만들었으며, 안쪽 리스트에는 해당 정점이 인접한 정점을 나타낸다.  
그래프 완전 탐색 방식에서는 해당 그래프의 정점이 방문여부를 확인하고, 방문하였다면 재접근을 막아야한다.  
그러므로 그래프 정점의 수와 같은 visited 리스트를 만들어서 방문여부를 확인한다.

### __DFS__
```python
def dfs(graph,start,visited):
    visited[start] = True
    print(start,end=" ")
    for i in graph[start]:
        if not visitied[i]:
            dfs(graph,i,visitied)
```
우선 함수를 시작할 때, 시작 정점을 방문했음을 남긴다. 그리고 해당 정점과 연결되어있는 인접 정점들을 루프를 통해 탐색을 시작한다. 루프를 도는 도중 만약 인접 정점이 거쳐가지 않았다면, 해당 정점을 시작 정점으로하는 dfs함수를 다시 실행한다.  
   
소스코드를 보면 재귀함수를 이용하는데, 재귀함수의 작동 방식 또한 스택으로 이루어진다. 그래서 굳이 스택을 사용하지 않고 재귀함수를 이용하여 dfs를 구현하는 것 또한 가능하다.

### __BFS__
```python
from collections import deque

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
```
BFS는 Queue를 이용하므로, Python에서는 ```collections``` 모듈을 이용하여 Queue를 사용한다.  
함수를 가장 먼저 시작하면 시작정점이 있는 queue를 생성하고, 해당 정점을 방문했음을 나타낸다.  
그리고 반복문을 실행하는데, 해당 반복문은 모든 정점을 방문할 때 까지 실행되어야한다. 모든 정점을 방문 했다는 것은, Queue에 어떤 것도 넣을 수 없고, Queue 또한 비어있다는 뜻이 된다.  
반복문 내부에는 하나씩 queue에 들어있는 정점을 꺼내어 정점과 연결된 정점이 한번 거쳐간 정점인지 아닌지를 판별한다. 거쳐가지 않았다면 queue에 해당 정점을 넣고, 방문표시를 한다.

## 📌 응용
코딩 테스트나, 연습문제들을 살펴보면 DFS/BFS를 이용하여 2차원 좌표에 상하좌우 좌표 이동을 하여 문제를 해결한다.  
주로 방향벡터를 처리할 때는 BFS를 이용하는데 아래의 BFS의 부분을 응용하여 문제를 해결한다.
```python
        n = queue.popleft()
        print(n,end=' ')
        for i in graph[n]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
```
아래 부분은 인접 그래프가 방문한 흔적이 없다면 queue에 삽입하여 bfs를 진행한다.  
그렇다면 만약 시작점에서 인접한 상 하 좌 우를 조사하여 조건에 맞다면 Queue에 넣어 조건에 맞는 인접한 노드에서 다시 상 하 좌 우를 조사할 수 있다. 이 행동을 반복한다면 모든 2차원 좌표를 조사할 수 있게 된다.

### __예제 문제 - 미로 탐색__
```python
from collections import deque


n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print (bfs(0,0))
```
상하좌우를 탐색하기 위한 dx,dy 리스트를 이용한다. 해당 리스트는 BFS 함수 내부의 반복에서 상하좌우를 탐색하도록 만든다. 그리고 탐색 위치의 상하좌우가 조건에 맞는 경우 Queue에 삽입하여 다음 반복에서 해당 지점에서 다시 상하좌우를 탐색하도록 코드가 짜여져있다.
