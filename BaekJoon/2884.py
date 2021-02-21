H,M=input().split()

H = int(H)
M = int(M)

M = M-45
if M<0:
    M=60+M
    H=H-1
    if H < 0:
        H = 23
    print(str(H)+" "+str(M))
else:print(str(H)+" "+str(M))