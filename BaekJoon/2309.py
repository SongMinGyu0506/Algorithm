import sys


list_height = []
for i in range(9):
    list_height.append(int(sys.stdin.readline()))

result_i = 0
result_j = 0
sum_list_height = sum(list_height)
for i in range(len(list_height)):
    for j in range(i+1,len(list_height)):
        if sum_list_height-(list_height[i]+list_height[j]) == 100:
            result_i = i
            result_j = j
            break

for i in sorted(list_height):
    if i != list_height[result_i] and i != list_height[result_j]:
        print(i)
