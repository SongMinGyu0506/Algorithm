from re import S
import sys


N = int(sys.stdin.readline())
data = []
for i in range(N):
    data.append(list(map(int,sys.stdin.readline().split())))

# def solution(data,start_point,money,max_day):
#     if start_point == N:
#         return money
#     if data[start_point][0] > max_day:
#         return money
#     tmp_money = money + data[start_point][1]
#     next_point = start_point + data[start_point][0]
#     tmp_max = max_day - data[start_point][0]
#     if N-start_point < data[start_point][0]:
#         return tmp_money
#     else:
#         tmp_money = solution(data,next_point,tmp_money,tmp_max)
#     return tmp_money

def solution(data,start_point,money,max_day):
    if max_day == 1:
        return money
    if start_point+data[start_point][0] > N:
        return money
    if max_day < data[start_point][0]:
        return money
    money = solution(data,start_point+data[start_point][0],money+data[start_point][1],max_day-data[start_point][0])
    return money

result_money_list = []
for i in range(N):
    result_money_list.append(solution(data,i,0,N))

print(result_money_list)

