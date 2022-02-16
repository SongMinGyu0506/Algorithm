N = int(input())
sort_list = []
for i in range(N):
    tmp_list = list(map(int,input().split()))
    sort_list.append(tmp_list)

sort_list.sort(key= lambda x: (x[1],x[0]))
for i in sort_list:
    print(i[0],i[1])
