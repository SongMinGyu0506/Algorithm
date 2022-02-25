from collections import deque
import sys


t = int(input())
for i in range(t):
    n,m = map(int,input().split())
    input_list = list(map(int,sys.stdin.readline().split()))
    test = []
    for i in range(len(input_list)):
        test.append([input_list[i],i])
    test = deque(test)
#test = deque([[5,0]])

    cnt = 0 
    while test:
        max_test = max(test)
        if test[0][0] == max_test[0]:
            cnt += 1
            if m == test[0][1]:
                print(cnt)
                break
            test.popleft()
        else:
            test.append(test.popleft())