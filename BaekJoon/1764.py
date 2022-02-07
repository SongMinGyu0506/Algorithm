import sys


N,M = map(int,sys.stdin.readline().split())
hear = set()
see = set()
for i in range(N):
    hear.add(sys.stdin.readline().strip('\n'))
for i in range(M):
    see.add(sys.stdin.readline().strip('\n'))


result = []
for i in hear:
    if i in see:
        result.append(i)

print(len(result))
for i in sorted(result):
    print(i)

