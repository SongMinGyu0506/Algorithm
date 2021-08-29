rom sys import stdin, stdout

n = stdin.readline()
N = sorted(map(int,stdin.readline().split()))
m = stdin.readline()
M = list(map(int, stdin.readline().split()))



def binary_search(array,target,start,end):
    if start > end:
        return 0
    mid = (start+end)//2
    if array[mid] == target:
        return 1
    elif target < array[mid]:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

for i in M:
  print(binary_search(N,i,0,len(N)-1))
