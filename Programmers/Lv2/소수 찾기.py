from itertools import permutations
def solution(numbers):
    answer = 0
    tmpList = []
    tmpIterList = []
    counter = 0
    
    for i in numbers:
        tmpList.append(i)
        
    for i in range(1,len(numbers)+1):
        for j in permutations(tmpList,i):
            tmpIterList.append(int(("").join(j)))
            
    tmpIterList = list(set(tmpIterList))

    if 0 in tmpIterList: 
        tmpIterList.remove(0)
    if 1 in tmpIterList:
        tmpIterList.remove(1)

    for i in tmpIterList:
        if i != 2 and i % 2 == 0:
            continue
        for j in range(1,i+1):
            if i % j == 0:
                counter = counter + 1
        if counter == 2:
            answer = answer + 1
        counter = 0
        
    return answer
