n = int(input())

memo = [0] * 90

memo[0] = 1
memo[1] = 1
memo[2] = 2

if n < 3:
    print(memo[n-1])
else:
    for i in range(3,n):
        memo[i] = memo[i-2] + memo[i-1]
    print(memo[n-1])