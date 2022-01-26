import sys

c = int(input())
for i in range(c):
    st_list = list(map(int,sys.stdin.readline().split()))
    avg = sum(st_list[1:])/st_list[0]

    cnt = 0
    for i in st_list[1:]:
        if avg < i:
            cnt += 1

    print("{:.3f}%".format((cnt/st_list[0]*100)))