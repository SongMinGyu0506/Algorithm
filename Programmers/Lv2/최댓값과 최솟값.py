def solution(s):
    answer = ''
    tmpS = s.split(" ")
    tmpIntS = []
    minnum = 0
    maxnum = 0
    for i in tmpS:
        tmpIntS.append(int(i))
    minnum = str(min(tmpIntS))
    maxnum = str(max(tmpIntS))
    return minnum+" "+maxnum
