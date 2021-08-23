def solution(s):
    answer = False
    if len(s) > 8 or len(s) < 0:
        return False
    if len(s) == 4 or len(s) == 6:
        answer = True
    for i in s:
        if (ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122):
            return False
    return answer
