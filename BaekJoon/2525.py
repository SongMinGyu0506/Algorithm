T,M = map(int,input().split())
P = int(input())

if M + P >= 60:
    T += (M+P)//60
    M = (M+P)%60
else:
    M = M + P
if T >= 24:
    T = T % 24
print(T,M)