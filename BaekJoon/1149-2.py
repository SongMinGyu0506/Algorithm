N = int(input())
dataArray = []
da = [0]*N
for i in range(N):
    a = list(map(int,input().split(' ')))
    dataArray.append(a)

da[0] = dataArray[0]

for i in range(1,N):
    red = dataArray[i][0] + min(da[i-1][1],da[i-1][2])
    green = dataArray[i][1] + min(da[i-1][0],da[i-1][2])
    blue = dataArray[i][2] + min(da[i-1][0],da[i-1][1])
    da[i] = [red,green,blue]

print(min(da[len(da)-1]))

