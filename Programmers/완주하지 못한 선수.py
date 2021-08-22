def solution(participant, completion):
    hashlist = {}
    for i in participant:
        if i in hashlist:
            hashlist[i] += 1
        else : hashlist[i] = 1
    for i in completion:
        if hashlist[i] == 1:
            del hashlist[i]
        else: hashlist[i] -= 1
    return list(hashlist.keys())[0]
