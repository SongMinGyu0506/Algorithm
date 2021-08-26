def solution(s):
    answer = ''
    tmp = []
    
    #전체 소문자화, 첫 문자 대문자 변환 capitalize()
    for i in s.split(' '):
        i = i.lower()
        i = i.capitalize()
        tmp.append(i)
        
    # 다시 문자열로 변환
    answer = ' '.join(tmp)
            
    return answer
