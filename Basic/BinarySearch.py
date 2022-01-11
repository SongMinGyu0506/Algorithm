testArray = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def Recursion_binarySearch(testArray,target):
    max = len(testArray)-1
    min = 0
    mid = len(testArray)//2

    if max < min:
        return False
    if target == testArray[mid]:
        return True
    elif target > testArray[mid]:
        return Recursion_binarySearch(testArray[mid+1:max+1],target)
    elif target < testArray[mid]:
        return Recursion_binarySearch(testArray[min:mid],target)

print(Recursion_binarySearch(testArray,8))
print(Recursion_binarySearch(testArray,13))
print(Recursion_binarySearch(testArray,123))

def Loop_binarySearch(testArray,target):
    max = len(testArray)-1
    min = 0
    mid = len(testArray)//2

    while min < max:
        if target == testArray[mid]:
            return True
        elif target > testArray[mid]:
            min = mid + 1
            mid = (min+max)//2
        elif target < testArray[mid]:
            max = mid
            mid = (min+max)//2
    return False

print()
print('Loop')
print(Loop_binarySearch(testArray,8))
print(Loop_binarySearch(testArray,13))
print(Loop_binarySearch(testArray,123))
print(Loop_binarySearch(testArray,-1))
print(Loop_binarySearch(testArray,0))
print(Loop_binarySearch(testArray,3.5))

testArray = [0,1,2,3,4,5,6,7,7,7,7,7,7,7,7,8,9,10,11,12,13,14,15]

def Upper_Bound(testArray,target):
    max = len(testArray)-1
    min = 0
    mid = len(testArray)//2

    while min < max:
        if target == testArray[mid]:
            return mid
            #return testArray[mid]
        elif target > testArray[mid]:
            min = mid + 1
            mid = (min+max)//2
        elif target < testArray[mid]:
            max = mid
            mid = (min+max)//2
    return max
    #return testArray[max]

print(Upper_Bound(testArray,7))

def Lower_Bound(testArray,target):
    max = len(testArray)-1
    min = 0
    mid = len(testArray)//2

    while min < max:
        if target == testArray[mid]:
            return testArray[mid]
        elif target > testArray[mid]:
            min = mid + 1
            mid = (min+max)//2
        elif target < testArray[mid]:
            max = mid
            mid = (min+max)//2
    if target > testArray[max-1] and target > testArray[max]:
        return testArray[max]
    else: 
        return testArray[max-1]

print (Lower_Bound(testArray,14.8))
    
print("test")
def upperBound(start, end, key):
    while start < end:
        mid = (start + end) // 2
        if lst[mid] == key:
            start = mid + 1
        elif lst[mid] < key:
            start = mid + 1
        elif key < lst[mid]:
            end = mid
    return end
    
lst = [0, 1, 2, 3, 3, 5, 6, 7, 8]
print(upperBound(0, len(lst), 3))