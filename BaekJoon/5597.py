import sys

n_list = sorted([int(sys.stdin.readline()) for i in range(28)])
n_list = [i for i in range(1,31) if i not in n_list]
for i in n_list:
    print(i)
