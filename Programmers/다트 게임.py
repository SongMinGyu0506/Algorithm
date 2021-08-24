def solution(dartResult):
    tmpDartResult = list(dartResult)
    score = []
    templistDart = []
    
    #문자 처리
    for i in range(len(tmpDartResult)):
        if tmpDartResult[i] == '1' and tmpDartResult[ia+1] == '0':
            templistDart.append('10')
        elif tmpDartResult[i] == '0' and tmpDartResult[i-1] == '1':
            continue
        else:
            templistDart.append(tmpDartResult[i])
    
    #점수 계산
    for i in range(len(templistDart)):
        if templistDart[i] == 'S':
            score.append(int(templistDart[i-1])**1)
        if templistDart[i] == 'D':
            score.append(int(templistDart[i-1])**2)
        if templistDart[i] == 'T':
            score.append(int(templistDart[i-1])**3)
        if templistDart[i] == '*':
            tempindex = len(score) - 1
            if tempindex == 0:
                score[tempindex] = score[tempindex] * 2
            else:
                score[tempindex] = score[tempindex] * 2
                score[tempindex - 1] = score[tempindex - 1] * 2
        if templistDart[i] == '#':
            tempindex = len(score) - 1
            score[tempindex] = score[tempindex] * (-1)
            
    print(score)
    return sum(score)
