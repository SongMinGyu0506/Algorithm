def solution(n):
    answer = ''
    soobak = "수박"
    soo = "수"
    
    s = n//2
    k = n%2
    print(s,k)
    for i in range(s):
        answer += soobak
    if k == 1:
        answer += soo
    
    return answer
