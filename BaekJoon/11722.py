import sys


N = int(sys.stdin.readline())
listA = list(map(int,sys.stdin.readline().split()))

dp = [0] * N

for i in range(len(listA)):
    dp[i] = 1
    for j in range(i):
        if listA[j] > listA[i]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))

# cnt = 1
# for i in range(len(dp)):
#     if dp[i] == cnt:
#         print(listA[dp.index(cnt)],end=' ')
#         cnt += 1
# print()