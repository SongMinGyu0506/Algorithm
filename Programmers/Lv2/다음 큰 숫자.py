def solution(n):
    answer = 0
    one = bin(n)[2:].count('1')
    n = n + 1
    while True:
        if bin(n)[2:].count('1') == one:
            answer = n
            break
        n = n + 1
    
    return answer
