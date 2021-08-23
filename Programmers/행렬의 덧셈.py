def solution(arr1, arr2):
    answer = [[]]
    size = len(arr1[1])
    for i in range(0,len(arr1)):
        for j in range(0,len(arr1[0])):
            arr1[i][j] = arr1[i][j] + arr2[i][j]
    answer = arr1
    return answer
