array = []
n = int(input())
for i in range(n):
    array.append(int(input()))

array.sort(reverse=True)

for i in array:
    print(i,end=' ')