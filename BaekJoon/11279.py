import heapq
import sys

hq = []
N = int(sys.stdin.readline())

cnt = 0
for i in range(N):
    number = int(sys.stdin.readline())
    if number == 0:
        if len(hq) == 0:
            print(0)
        else:
            print(heapq.heappop(hq)*-1)
    else:
        heapq.heappush(hq,-number)

