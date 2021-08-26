def solution(price, money, count):
    answer = -1
    tmp = 0
    for i in range(1,count+1):
        tmp = tmp + price*i
    if money < tmp:
        answer = tmp - money
    else:
        answer = 0
    return answer
