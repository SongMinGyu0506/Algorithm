import sys


T = int(sys.stdin.readline())
for i in range(T):
    a,b = map(int,sys.stdin.readline().split())
    if a == 1:
        print(1)
    else:
        dataset = a**b
        if dataset < 11:
            print(dataset%11)
        else:
            print(str(dataset)[-1])
