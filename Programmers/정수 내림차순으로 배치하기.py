def solution(n):
    temp = list(str(n))
    temp.sort(reverse=True)
    answer =''
    for i in temp:
        answer = answer + i
    return int(answer)
