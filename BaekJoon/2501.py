import sys


N,K = map(int,sys.stdin.readline().split())
result_list = []
for i in range(1,N+1):
    if N%i == 0:
        result_list.append(i)

if len(result_list) == 0:
    result_list = [0]*10000

result_list = sorted(result_list)


if len(result_list) < K:
    print(0)
else:
    print(result_list[K-1])
