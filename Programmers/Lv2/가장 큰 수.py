def solution(numbers):
    answer=''
    numbers = list(map(str,numbers))

    #string sort의 기준 앞글자 하나씩 부터 비교 앞글자가 같다면 뒷글자 차이날때까지 비교함
    #동일한 기준을 만들기 위해서 numbers 원소의 최소값 또한 numbers의 최대치인 1000 근처까지 끌어올려서 동일 기준으로 비교 시작
    numbers.sort(key=lambda x: x*3, reverse=True)

    #0만 무수히 들어가면 중복 제거를 위해서 해당 작업 실시
    answer = str(int(''.join(numbers)))
    return answer


numbers1 = [6,10,2]
numbers2 = [3,30,34,5,9]

print(solution(numbers1))
print(solution(numbers2))