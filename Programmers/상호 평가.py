def solution(scores):
    tmpScores = []
    answer = ''
    average = []
    
    for i in range(len(scores)):
        tmp = []
        for j in range(len(scores)):
            tmp.append(scores[j][i])
        tmpScores.append(tmp)
        
    for i in range(len(tmpScores)):
        if tmpScores[i][i] == max(tmpScores[i]) and tmpScores[i].count(max(tmpScores[i])) == 1:
            del tmpScores[i][i]
            continue
        if tmpScores[i][i] == min(tmpScores[i]) and tmpScores[i].count(min(tmpScores[i])) == 1:
            del tmpScores[i][i]
            continue
    
    for i in range(len(tmpScores)):
        average.append(sum(tmpScores[i])/len(tmpScores[i]))
        
    for i in average:
        if i >= 90:
            answer = answer + 'A'
        elif i < 90 and i >= 80:
            answer = answer + 'B'
        elif i < 80 and i >= 70:
            answer = answer + 'C'
        elif i < 70 and i >= 50:
            answer = answer + 'D'
        else:
            answer = answer + 'F'
    return answer
