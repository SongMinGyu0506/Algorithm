n = int(input())
input_list = list(map(int,input().split()))
m = int(input())
x = list(map(int,input().split()))

def binary_search(array,target,start,end):
    if start > end:
        return None
    mid = (start+end)//2
    if array[mid] == target:
        return 'yes'
    if array[mid] > target:
        return binary_search(array,target,start,mid-1)
    if array[mid] < target:
        return binary_search(array,target,mid+1,end)

for i in x:
    result = binary_search(input_list,i,0,n-1)
    if result == None:
        print('no',end=' ')
    else:
        print('yes',end=' ')