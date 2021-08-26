def solution(s):
    answer = 0
    if '-' in s:
        s = s.replace('-','')
        s = int(s) * (-1)
        answer = s
    else:
        s = int(s)
        answer = s
    return answer
