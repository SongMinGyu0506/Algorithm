from collections import deque
import sys


T = int(sys.stdin.readline())



stack = deque()
for i in range(T):
    num = int(sys.stdin.readline())
    if num != 0:
        stack.append(num)
    else:
        stack.pop()

if len(stack) == 0:
    print(0)
else:
    print(sum(stack))