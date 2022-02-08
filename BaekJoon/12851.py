import sys
from collections import deque, Counter

visited = set()
result = []
def bfs(start,end):
    que = deque()
    que.append((start,0))

    while que:
        point, cnt = que.popleft()
        if point not in visited:
            if point == end:
                result.append(cnt)
            if point != end:
                visited.add(point)
                
            if 0 <= point-1 <= 100000 and point-1:
                que.append((point-1,cnt+1))
            if 0 <= point+1 <= 100000 and point+1:
                que.append((point+1,cnt+1))
            if 0 <= point*2 <= 100000 and point*2:
                que.append((point*2,cnt+1))


N,K = map(int,sys.stdin.readline().split())
bfs(N,K)
print(min(result))
print(Counter(result)[min(result)])

