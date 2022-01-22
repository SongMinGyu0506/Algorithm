n = int(input())

memo = []

memo.append(1)
memo.append(2)

if n < 3:
    print(memo[n-1])
else:
    for i in range(2,n):
        memo.append(memo[i-2]+memo[i-1])
    print(memo[n-1]%10007)
