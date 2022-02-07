import sys
from collections import deque

visited = set()
def bfs(start,end):
    que = deque()
    que.append((start,0))
    visited.add(start)
    while que:
        point, cnt = que.popleft()
        if point == end:
            return cnt
        
        if 0 <= point-1 <= 100000 and point-1 not in visited:
            que.append((point-1,cnt+1))
            visited.add(point-1)
        if 0 <= point+1 <= 100000 and point+1 not in visited:
            que.append((point+1,cnt+1))
            visited.add(point+1)
        if 0 <= point*2 <= 100000 and point*2 not in visited:
            que.append((point*2,cnt+1))
            visited.add(point*2)


N,K = map(int,sys.stdin.readline().split())
print(bfs(N,K))

