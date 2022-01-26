import sys


N = int(sys.stdin.readline())
cnt = 0
word = []
for i in range(N):
    word_dic = {}
    word.append(sys.stdin.readline())


for i in range(len(word)):
    is_count = True
    word_dic = {}
    if len(word[i]) == 1:
        cnt += 1
    else:
        for j in range(len(word[i])):
            try:
                if word_dic[word[i][j]] == 1 and (word[i][j-1] != word[i][j]):
                    is_count = False
                    break
            except:
                word_dic[word[i][j]] = 1
    if is_count:
        cnt+=1

print(cnt)

