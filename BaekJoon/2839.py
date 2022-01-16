N = int(input())
dn = [float("inf")]*5001
if len(dn) < 6:
    print(-1)
else:
    dn[3] = 1
    dn[5] = 1
    for i in range(6,N+1):
        dn[i] = min(dn[i-3]+1,dn[i-5]+1)
    print(dn[0:N+1])
    print(dn[N])