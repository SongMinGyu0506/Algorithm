from bisect import bisect_left
import sys


N = int(sys.stdin.readline())
listA = list(map(int,sys.stdin.readline().split()))
dp = []
for i in range(len(listA)):
    if len(dp) == 0:
        dp.append(listA[i])
        continue
    if dp[-1] < listA[i]:
        dp.append(listA[i])
    else:
        dp[bisect_left(dp,listA[i])] = listA[i]

print(len(dp))
# for i in dp:
#     print(i,end=' ')
# print()