from collections import deque
import sys

N = int(sys.stdin.readline())
card = deque()

for i in range(1,N+1):
    card.append(i)

while card:
    if len(card)==1:
        print(card.pop())
        break
    card.popleft()
    card.append(card.popleft())
