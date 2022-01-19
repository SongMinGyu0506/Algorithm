t_case = int(input())
for i in range(t_case):
    N = int(input())
    memo = [1,1,1]
    for i in range(3,N):
        memo.append(memo[i-3]+memo[i-2])
    print(memo[len(memo)-1])