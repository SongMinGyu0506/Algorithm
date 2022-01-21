K, N = map(int,input().split(' '))
lan_cable = []
for i in range(K):
    tmp = int(input())
    lan_cable.append(tmp)

min = 0
maxs = max(lan_cable)

mid_array = []
if N == 1:
    print(max(lan_cable))
else:
    while min < maxs:
        mid = (min+maxs)//2
        result = 0
        for i in range(K):
            result = result + (lan_cable[i]//mid)
        if result == N:
            mid_array.append(mid)
            min = maxs - 1
        elif result < N:
            maxs = mid
        elif result > N:
            mid_array.append(mid)
            min = mid + 1
    print(max(mid_array))
