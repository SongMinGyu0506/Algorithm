N = int(input())
X = list(map(int,input().split(' ')))

X_rank = sorted(list(set(X)))

dic = {X_rank[i]:i for i in range(len(X_rank))}

for i in X:
    print(dic[i], end=' ')
print()