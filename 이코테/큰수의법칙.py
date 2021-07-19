n,m,k = map(int,input().split())
data=list(map(int,input().split()))
result = 0

data.sort()

first = data[n-1]
second = data[n-2]

m_counter = 0
k_counter = 0

while True:
    if m_counter == m: break
    if k_counter != k:
        k_counter += 1
        result = result + first
    else:
        result = result + second
        k_counter = 0
    m_counter += 1

print(result)

