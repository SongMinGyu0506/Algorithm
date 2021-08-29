def solution(s):
    answer = True
    calList = []
    for i in range(len(s)):
        if s[i] == '(':
            calList.append(s[i])
        if s[i] == ')':
            if '(' in calList:
                del calList[len(calList)-1]
            else:
                return False
    if len(calList) != 0:
        return False
    return True
