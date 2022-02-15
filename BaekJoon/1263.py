import sys
from collections import deque
N = int(sys.stdin.readline())
todoList = []
for i in range(N):
    T,S = map(int,sys.stdin.readline().split())
    todoList.append([T,S])
todoList = sorted(todoList,key=lambda x:x[1])

time = -1
timelist = []
if todoList[0][1] - todoList[0][0] < 0:
    print(time)
else:
    for i in range(todoList[0][1] - todoList[0][0],-1,-1):
        breakPoint = False
        tmp = i
        for todo in todoList:
            if todo[0] + tmp > todo[1]:
                breakPoint = True
                break
            else:
                tmp += todo[0]
        if breakPoint == False:
            timelist.append(i)
if len(timelist) == 0:
    print(-1)
else:
    print(max(timelist))


# 0~2
# 2~9
# 9~10
# 10~14