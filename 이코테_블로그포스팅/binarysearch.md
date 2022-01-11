# 📖이진(분) 탐색 (Binary Search)


## 📌서론
알고리즘 및 코딩테스트 문제에서 등장하는 탐색 방법 중 하나,  
이진 탐색 자체는 어렵지 않으나, 문제에서는 여러가지 개념을 섞어서 나온다면 문제가 상당히 어려워질 수 있다.  
그래서 이진 탐색의 개념을 확실히 정리하고 넘어 가는 것 또한 매우 중요하다고 생각하여 이진 탐색을 정리하여 포스팅한다.

## 📌특징
* 탐색이 되는 주체(리스트 및 배열)가 정렬이 되어있는 상태여야만 Binary Search가 가능하다.
* 시작, 중간, 끝 값을 가지고 탐색을 진행, 데이터를 반씩 쪼개어서 탐색을 시도
* 해당 방법으로 빠른 시간으로 원하는 값을 찾는 것이 가능하다. ```logN``` 소요

## 📌구현
구현의 방법에는 여러가지 방법이 있는데,  
재귀(Recursion)을 이용한 방법, 반복을 이용한 방법으로 구현해 본다.  
구현 방법에는 여러가지가 있겠지만, 가장 기본적인 중간 값을 비교하고, 타겟이 중간 값보다 크거나 작으면 중간 값을 기준으로 반으로 나눠서 다시 탐색을 진행하는 것은 같다.

### 재귀(Recursion) 이용
```python
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
```

### 반복(Loop) 이용
```python
def Loop_binarySearch(testArray,target):
    max = len(testArray)-1
    min = 0
    mid = len(testArray)//2

    while min < max:
        if target == testArray[mid]:
            return mid #위치
        elif target > testArray[mid]:
            min = mid + 1
            mid = (min+max)//2
        elif target < testArray[mid]:
            max = mid
            mid = (min+max)//2
    return False
```

## 📌추가- Upper/Lower Bound
앞에서의 Binary Search는 값을 찾지 못한다면, ```False```를 반환하도록 되어있다.  
하지만, 필요에 따라 ```False```가 아닌 비슷하거나 근처의 값을 반환하거나, 
같은 중복된 수가 있다면 얼마 만큼 떨어져 있는지 필요한 경우가 있다. 이 경우 찾는 값 다음으로 크거나 작은 값을 필요로 한다.  
이 경우 또한 이진 탐색의 방법을 이용하여 구현한다. 
### 구현(Upper Bound)
```Python
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
```