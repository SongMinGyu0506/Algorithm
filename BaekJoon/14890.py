from collections import Counter


#입력 부분
N, L = input().split()
N = int(N)
L = int(L)
cnt = 0 #최종 결과


#이차원 배열로 입력받기
raw_arr = [0 for _ in range(N)]
for i in range(N):    
	raw_arr[i] = list(map(int, input().split()))

#세로부분 탐색하기 위해서 행 열 뒤집기
reverse_arr = list(map(list,zip(*raw_arr)))

#가로부분 탐색 시작
for i in range(N):
    pre = raw_arr[i][0] #이전 배열 값
    in_count = 1 # 시작이므로 무조건 1
    if int(len(Counter(raw_arr[i]).keys()) == int(1)): #만약 한줄이 통째로 같은 수로 되어있다면? 카운트 추가하고 continue
        cnt += 1
        continue
    for j in range(1,N):
        #case1 이전 수와 현재 위치의 수가 같은경우
        if raw_arr[i][j] == pre: 
            in_count+=1
            pre = raw_arr[i][j]
        #case2 이전 수보다 현재 위치의 수가 더 높고, 카운팅 수가 0보다 높다(내리막길과 겹치지 않아야함)
        elif raw_arr[i][j] == pre+1 and in_count >= 0:
            # 이때 조건보다 여유블록이 많을경우 카운터 초기화하고 이전 값을 현재위치로 만듬(정상)
            if in_count >= L:
                in_count = 1 
                pre = raw_arr[i][j]
            #조건 부적합으로 break
            else:
                break
        #case3 내리막길의 경우, 현재 위치가 이전 값보다 1 작아야하며, 이전 내리막길과 겹쳐서는 안됌(여유 블록이 필요함)
        elif raw_arr[i][j] == pre-1 and in_count >= 0:
            #조건만큼 맞춰야함 즉, 0을 맞추지 못하면 블록 부족함 (해당줄 무조건 실패)
            in_count = -L+1
            pre = raw_arr[i][j]
        else:
            break;
    else:
        #여유 블록이 0보다 크다면 해당줄은 성공
        if in_count >= 0:
            cnt +=1


for i in range(len(reverse_arr)):
    pre = reverse_arr[i][0]
    in_count = 1
    if int(len(Counter(reverse_arr[i]).keys()) == int(1)):
        cnt += 1
        continue
    for j in range(1,N):
        if reverse_arr[i][j] == pre: 
            in_count+=1
            pre = reverse_arr[i][j]
        elif reverse_arr[i][j] == pre+1 and in_count >= 0:
            if in_count >= L:
                in_count = 1
                pre = reverse_arr[i][j]
            else:
                break
        elif reverse_arr[i][j] == pre-1 and in_count >= 0:
            in_count = -L+1
            pre = reverse_arr[i][j]
        else:
            break;
    else:
        if in_count >= 0:
            cnt +=1
    #print(len(Counter(raw_arr[i]).keys()))

print(cnt)
