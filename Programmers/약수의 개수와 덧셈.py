def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        counter = 0
        for j in range(1,i+1):
            if i%j == 0:
                counter = counter + 1
        if counter % 2 == 0:
            answer = answer + i
        else:
            answer = answer + (-i)
    return answer
