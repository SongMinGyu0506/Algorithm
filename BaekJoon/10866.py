from collections import deque
import sys
Deque = deque()

N = int(input())

for i in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == 'push_front':
        Deque.appendleft(command[1])
    elif command[0] == 'push_back':
        Deque.append(command[1])
    elif command[0] == 'pop_front':
        if not Deque:
            print(-1)
        else:
            print(Deque.popleft())
    elif command[0] == 'pop_back':
        if not Deque:
            print(-1)
        else:
            print(Deque.pop())
    elif command[0] == 'size':
        print(len(Deque))
    elif command[0] == 'empty':
        if not Deque:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not Deque:
            print(-1)
        else:
            print(Deque[0])
    elif command[0] == 'back':
        if not Deque:
            print(-1)
        else:
            print(Deque[len(Deque)-1])

    