def solution(N, stages):
    result = {}
    player = len(stages)
    for i in range(1,N+1):
        if player != 0:
            result[i] = stages.count(i) / player
            player -= stages.count(i)
        else:
            result[i] = 0
    return sorted(result,key=lambda x : result[x], reverse=True)
