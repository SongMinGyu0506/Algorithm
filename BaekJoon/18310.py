N = int(input())
home_list = list(map(int,input().split()))

home_list.sort()

if len(home_list)%2 == 1:
    print(home_list[len(home_list)//2])
else:
    mid1 = len(home_list)//2
    mid2 = (len(home_list)//2)-1
    tmp_list1 = []
    tmp_list2 = []
    for i in home_list:
        tmp_list1.append(abs(i-mid1))
        tmp_list2.append(abs(i-mid2))
    tmp_list11 = sum(tmp_list1)
    tmp_list22 = sum(tmp_list2)
    if tmp_list1 > tmp_list2:
        print(home_list[mid2])
    elif sum(tmp_list1) == sum(tmp_list2):
        print(min(mid1,mid2))
    else:
        print(home_list[mid1])
