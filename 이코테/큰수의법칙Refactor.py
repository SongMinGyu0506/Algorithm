n,m,k = map(int,input().split())
data = list(map(int,input().split()))
result = 0

data.sort()

first = data[n-1]
second = data[n-1]

count = int(((m/(k+1))*k) + (m%(k+1)))

result = result + (count*first)
result = result + ((m-count)*second)

print(result)