n,m = map(int,input().split())

result = 0

for i in range(n):
    data = list(map(int,input().split()))
    min_data = min(data)
    if result < min_data:
        result = min_data

print(result)