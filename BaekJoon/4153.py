while True:
    A = list(map(int,input().split()))
    if A[0] == 0 and A[1] == 0 and A[2] == 0:
        break
    A.sort()
    maxA = A[-1]
    A = A[0:2]
    if A[0] ** 2 + A[1] ** 2 == maxA ** 2:
        print('right')
    else:
        print('wrong')