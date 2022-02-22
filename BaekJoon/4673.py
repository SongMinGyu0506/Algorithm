tmp_list = set([i for i in range(1,10001)])
tmp2 = set()
for i in range(1,10001):
    result_i = i
    tmp = i
    while True:
        ttmp_i = tmp % 10
        result_i += ttmp_i
        tmp = tmp // 10
        if tmp < 10:
            result_i += tmp
            break
    tmp2.add(result_i)

for i in sorted(tmp_list - tmp2):
    print(i)

