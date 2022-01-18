N = int(input())
dataArray = []
da = [0]*N
for i in range(N):
    a = list(map(int,input().split(' ')))
    dataArray.append(a)

da[0] = min(dataArray[0][0],dataArray[0][1],dataArray[0][2])
da_index = dataArray[0].index(da[0])
dataArray[1][da_index] = float("inf")

for i in range(1,N-1):
    da[i] = min(da[i-1]+dataArray[i][0],da[i-1]+dataArray[i][1],da[i-1]+dataArray[i][2])
    da_index = dataArray[i].index(da[i]-da[i-1])
    dataArray[i+1][da_index] = float("inf")

da[len(da)-1] = min(da[len(da)-2]+dataArray[len(dataArray)-1][0],da[len(da)-2]+dataArray[len(dataArray)-1][1],da[len(da)-2]+dataArray[len(dataArray)-1][2])

print(da[len(da)-1])
