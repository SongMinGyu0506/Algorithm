from pprint import pprint
import sys

N,M = map(int,input().split())

data = {}
for i in range(N):
    site,pwd = sys.stdin.readline().split()
    data[site] = pwd

for i in range(M):
    site = sys.stdin.readline()
    site = site[:-1]
    print(data[site])