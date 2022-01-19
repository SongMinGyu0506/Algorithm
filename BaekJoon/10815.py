N = int(input())
N_array = list(map(int,input().split(' ')))
M = int(input())
M_array = list(map(int,input().split(' ')))

M_array_hash = {}

for i in M_array:
    M_array_hash[i] = 0

N_array = sorted(N_array)
M_array = sorted(M_array)

for i in M_array:
    start = 0
    end = len(N_array)
    while start < end:
        mid = (start + end) // 2
        if N_array[mid] == i:
            M_array_hash[i] = 1
            break
        elif N_array[mid] < i:
            start = mid + 1
        elif N_array[mid] > i:
            end = mid

for key,value in M_array_hash.items():
    print(value ,end=' ')
print()

