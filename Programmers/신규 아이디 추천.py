def solution(new_id):
    answer = new_id
    temp = ''
    #first
    answer = answer.lower()
    
    #second
    for i in answer:
        for j in range(97,123):
            temp = chr(j)
            if i == temp: break
        if i == temp:
            temp = ''
            continue
        for j in range(48,58):
            temp = chr(j)
            if i == temp: break
        if i == temp:
            temp = ''
            continue
            
        if i == '.': continue
        elif i == '-': continue
        elif i == '_': continue
        else: answer = answer.replace(i,"")

    #third
    while ".." in answer:
        answer = answer.replace("..",".")
        
    #fourth
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    
    #fibth
    answer ="a" if answer == '' else answer
    
    #six
    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer[1:] if answer[0] == '.' and len(answer) > 1 else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    
    while len(answer) < 3:
        answer = answer + answer[-1]
    
    
    return answer