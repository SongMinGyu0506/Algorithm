def solution(arr):
    answer = []
    if len(arr) == 1:
        answer.append(-1)
        return answer
    del arr[arr.index(min(arr))]
    for i in arr:
        answer.append(i)
    return answer
