import sys
from collections import Counter


N = (int(sys.stdin.readline()))
original_list = [int(sys.stdin.readline()) for i in range(N)]

print(int(round(sum(original_list) / len(original_list),0)))
print(sorted(original_list)[len(original_list)//2])



mode = sorted(Counter(original_list).most_common(),key=lambda x : (-x[1],x[0]))
if len(mode) == 1:
    print(mode[0][0])
else:
    if mode[0][1] == mode [1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
print(max(original_list) - min(original_list))


