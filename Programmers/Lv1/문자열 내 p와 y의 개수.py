def solution(s):
    answer = True
    Pcounter = 0
    Ycounter = 0
    for i in s:
        if i == 'p' or i == 'P':
            Pcounter += 1
        if i == 'y' or i == 'Y':
            Ycounter += 1
    if Pcounter == Ycounter:
        answer = True
    else:
        answer = False
    return answer
