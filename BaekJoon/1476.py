import sys


E,S,M = map(int,sys.stdin.readline().split())

counting_E, counting_S, counting_M = 0,0,0
result = 0
while True:
    if counting_E == E and counting_S == S and counting_M == M:
        break
    counting_S += 1
    counting_E += 1
    counting_M += 1
    result += 1

    if counting_E == 16:
        counting_E = 1
    if counting_S == 29:
        counting_S = 1
    if counting_M == 20:
        counting_M = 1
print(result)