def solution(num):
    counter = 0
    answer = num
    while True:
        if counter == 500 and answer != 1:
            return -1
        if answer == 1:
            return counter
        
        counter += 1
        if answer % 2 == 0:
            answer = answer // 2
        else:
            answer = (answer * 3) + 1
