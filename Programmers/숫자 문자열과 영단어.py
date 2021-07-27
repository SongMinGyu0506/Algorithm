def solution(s):
    answer = s
    answer = answer.lower()
    if "zero" in answer:
        answer = answer.replace("zero","0")
    if "one" in answer:
        answer = answer.replace("one","1")
    if 'two' in answer:
        answer = answer.replace('two','2')
    if 'three' in answer:
        answer = answer.replace('three','3')
    if 'four' in answer:
        answer = answer.replace('four','4')
    if 'five' in answer:
        answer = answer.replace('five','5')
    if 'six' in answer:
        answer = answer.replace('six','6')
    if 'seven' in answer:
        answer = answer.replace('seven','7')
    if 'eight' in answer:
        answer = answer.replace('eight','8')
    if 'nine' in answer:
        answer = answer.replace('nine','9')
    return int(answer)

def solution2(s):
    answer = s
    answer = answer.lower()
    alphabet_list = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    for alphabet_key in alphabet_list:
        if alphabet_list[alphabet_key] in answer:
            answer = answer.replace(alphabet_list[alphabet_key],alphabet_key)
    return int(answer)
