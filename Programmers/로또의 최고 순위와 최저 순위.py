def ranking(x):
    if x == 6:
        return 1
    elif x == 5:
        return 2
    elif x == 4:
        return 3
    elif x == 3:
        return 4
    elif x == 2:
        return 5
    else:
        return 6

def solution(lottos, win_nums):
    answer = []
    zero_count = 0
    min_count = 0
    for i in win_nums:
        if i in lottos:
            min_count += 1
    answer.append(ranking(min_count))
    for i in lottos:
        if i == 0:
            zero_count += 1
    answer.append(ranking(min_count+zero_count))
    answer.sort()
    return answer

print(solution([44,1,0,0,31,25],[31,10,45,1,6,19]))
print(solution([0,0,0,0,0,0],[38,19,20,40,15,25]))
print(solution([45,4,35,20,3,9],[20,9,3,45,4,35]))