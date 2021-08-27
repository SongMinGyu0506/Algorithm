def solution(n):
    answer = 0
    for i in range(1,n+1):
        tmp = 0
        for j in range(i,n+1):
            tmp = tmp + j
            if tmp == n:
                answer = answer + 1
            if tmp > n:
                break
    return answer
