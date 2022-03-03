from collections import deque

n,k = map(int,input().split())
numbers = input()

stack = deque()
cnt = k
for number in numbers:
    while stack and cnt > 0 and stack[-1] < number:
        stack.pop()
        cnt -= 1
    stack.append(number)

stack = list(stack)
print(''.join(stack[:n-k]))

# 오답 이유 : 스택 제거시 한번만 작동하게 만듬

# 풀이 방법
'''
    가장 큰 수를 만들기 위해서는 가장 왼쪽에 제일 큰 수가 와야한다.
    일반적인 리스트를 사용하면 TLE가 걸림 --> 스택사용
    그리고 제가 가능한 횟수가 다되어도 스택에 계속 추가되므로 n - k만큼만
    출력해야함
'''