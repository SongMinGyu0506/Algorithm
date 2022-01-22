T = int(input())
for i in range(T):
    zero_counter = [1,0,1,1]
    one_counter = [0,1,1,2]
    n = int(input())
    if n < 4:
        print(zero_counter[n],one_counter[n])
    else:
        for i in range(4,n+1):
            zero_counter.append(zero_counter[i-2] + zero_counter[i-1])
            one_counter.append(one_counter[i-2] + one_counter[i-1])
        print(zero_counter[n],one_counter[n])