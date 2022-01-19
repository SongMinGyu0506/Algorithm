N = int(input())
A = list(map(int,input().split(' ')))
B,C = map(int,input().split(' '))

result = N
A_tmp = [i-B for i in A]
print(A_tmp)

for i in A_tmp:
    if i%C != 0:
        result = result + (i//C)+1
    else:
        result = result + (i//C)

print (result)