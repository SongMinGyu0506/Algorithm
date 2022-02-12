import sys


N = int(sys.stdin.readline())
tester = list(map(int,sys.stdin.readline().split()))
B,C = map(int,sys.stdin.readline().split())

result = N
for i in range(len(tester)):
    if tester[i] - B <= 0:
        tester[i] = 0
    else:
        tester[i] = tester[i] - B

for i in range(len(tester)):
    result = result + (tester[i]//C)
    if tester[i]//C >= 1 and tester[i]%C != 0:
        tester[i] = tester[i]%C
    if tester[i]//C == 0 and tester[i]%C != 0:
        result += 1

print(result)