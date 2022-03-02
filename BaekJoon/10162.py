T = int(input())
A_counter = 0
B_counter = 0
C_counter = 0
A = 300
B = 60
C = 10

if T%10 != 0:
    print(-1)
else:
    while T != 0:
        if T >= A:
            T -= A
            A_counter += 1
            continue
        if T >= B:
            T -= B
            B_counter += 1
            continue
        else:
            T -= C
            C_counter += 1
            continue
    print(A_counter,B_counter,C_counter)
