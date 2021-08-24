def solution(s):
    ordlist = []
    answer = ''
    for i in s:
        ordlist.append(ord(i))
    ordlist.sort(reverse=True)
    for i in range(len(ordlist)):
        ordlist[i] = chr(ordlist[i])
        answer = answer + ordlist[i]
    return answer
