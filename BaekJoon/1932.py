n = int(input())
array = []
for i in range(n):
    array.append(list(map(int,input().split())))

for i in range(1,n):
    for j in range(len(array[i])):
        if j == 0: array[i][j] += array[i-1][j]
        elif j == i: array[i][j] += array[i-1][j-1]
        else: array[i][j] += max(array[i-1][j-1],array[i-1][j])

print(max(array[-1]))