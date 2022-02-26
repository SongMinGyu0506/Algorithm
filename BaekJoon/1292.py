numbers = []

A,B = map(int,input().split())


for i in range(1,1001):
    for j in range(i):
        numbers.append(i)

print(sum(numbers[A-1:B]))