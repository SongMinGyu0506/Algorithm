array = list(map(int,input().split()))

if array[0] == 1:
    for i in range(1,8):
        if array[i] != array[i-1]+1:
            print('mixed')
            exit(0)
    print('ascending')
elif array[0] == 8:
    for i in range(1,8):
        if array[i] != array[i-1]-1:
            print('mixed')
            exit(0)
    print('descending')
else:
    print('mixed')
