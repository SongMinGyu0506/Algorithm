from collections import deque
import sys

final = []
T = int(sys.stdin.readline())
for i in range(T):
    reverse_counter = 'F'
    error_counter = 'F'
    #입력
    commands = sys.stdin.readline().strip('\n')
    array_size = int(sys.stdin.readline())
    string_array = sys.stdin.readline()

    #배열 데이터 가공
    setting_array = deque(string_array.strip('\n').replace('[','').replace(']','').split(','))

    # 커맨드 처리
    for command in commands:
        if command == 'R':
            if reverse_counter == 'F':
                reverse_counter = 'B'
            else:
                reverse_counter = 'F'
        if command == 'D':
            if len(setting_array) == 0 or setting_array[0] == '':
                error_counter = 'T'
                final.append('error')
                break
            if reverse_counter == 'B':
                setting_array.pop()
            else:
                setting_array.popleft()
    
    if error_counter == 'F':
        # B일 경우, 뒤집어야함
        if reverse_counter == 'B':
            setting_array.reverse()

        result = str(list(setting_array)).replace("'","").replace(' ','')
        final.append(result)

for i in final:
    print(i)