import sys


N = int(input())
print(*(x for x in sorted(list(set([sys.stdin.readline().rstrip('\n') for i in range(N)])),key=lambda x:(len(x),x))),sep='\n')