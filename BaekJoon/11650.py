import sys


N = int(sys.stdin.readline())
a = []
for i in range(N):
    x,y = map(int,sys.stdin.readline().split())
    a.append([x,y])

a.sort(key=lambda x: (x[0],x[1]))

for i in a:
    print(i[0],i[1])