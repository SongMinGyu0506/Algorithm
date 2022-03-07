


from collections import deque


T = int(input())
for i in range(T):
    counter = False
    string = deque(input())
    stack = deque()
    for i in string:
        if i == '(':
            stack.append('(')
            continue
        if not stack:
            counter = True
            print('NO')
            break
        else:
            stack.pop()
    if counter == False:
        if stack:
            print('NO')
        else:
            print('YES')
