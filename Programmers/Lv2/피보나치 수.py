def solution(n):
    bottomUp = []
    bottomUp.append(0)
    bottomUp.append(1)
    bottomUp.append(1)
    for i in range(3,n+1):
        bottomUp.append((bottomUp[i-1]+bottomUp[i-2])%1234567)
    return bottomUp[n]
