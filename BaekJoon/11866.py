from collections import deque


N,K = map(int,input().split())
sol_list = deque([i for i in range(1,N+1)])
result_list = []
cnt = 0

while sol_list:
    cnt += 1
    if cnt == K:
        tmp = sol_list.popleft()
        result_list.append(tmp)
        cnt = 0
    else:
        sol_list.append(sol_list.popleft())
        

result_list = str(result_list).replace('[','<').replace(']','>')
print(result_list)
