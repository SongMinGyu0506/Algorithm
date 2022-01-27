from collections import deque
import sys

def D_control(n):
    res = n*2
    if res > 9999:
        res %= 10000
    return res

def S_control(n):
    res = n
    if n == 0:
        res = 9999
        return res
    res -= 1
    return res

def L_switch(n):
    front = n % 1000
    back = n // 1000
    res = front*10 + back
    return res

def R_switch(n):
    front = n % 10
    back = n // 10
    res = front*1000 + back
    return res


def bfs(A,B):
    que = deque()
    que.append((A,""))
    visited = set()
    visited.add(A)
    while que:
        number, command = que.popleft()
        if number == B:
            print(command)
            return

        tmp = D_control(number)
        if tmp not in visited:
            visited.add(tmp)
            que.append((tmp,command+"D"))

        tmp = S_control(number)
        if tmp not in visited:
            visited.add(tmp)
            que.append((tmp,command+"S"))

        tmp = L_switch(number)
        if tmp not in visited:
            visited.add(tmp)
            que.append((tmp,command+"L"))

        tmp = R_switch(number)
        if tmp not in visited:
            visited.add(tmp)
            que.append((tmp,command+"R"))


T = int(sys.stdin.readline())
for i in range(T):
    A,B = map(int,sys.stdin.readline().split())
    bfs(A,B)
