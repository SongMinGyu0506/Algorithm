n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))
if len(array) == 1:
    print(array[0])
elif len(array) == 2:
    print(array[0]+array[1])
else:
    memo = []
    memo.append(array[0])
    memo.append(max(array[0]+array[1],array[1]))
    memo.append(max(array[0]+array[2],array[1]+array[2]))
    for i in range(3,n):
        memo.append(max(memo[i-3] + array[i-1] + array[i], memo[i-2]+array[i]))
    print(memo[n-1])