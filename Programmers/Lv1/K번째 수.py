def solution(array, commands):
    answer = []
    tmpArray = []
    for i in range(len(commands)):
        tmpArray.append(array[commands[i][0]-1:commands[i][1]])
    for i in range(len(tmpArray)):
        tmpArray[i].sort()
    for i in range(len(commands)):
        tmpNum = commands[i][2] -1
        answer.append(tmpArray[i][tmpNum])
        
        
    #print(tmpArray)
    return answer
