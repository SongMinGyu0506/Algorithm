def solution(x):
    answer = False
    strx = str(x)
    k = 0
    for i in strx:
        k += int(i)
    print(x%k)
    if x%k == 0:
        answer = True
    return answer
