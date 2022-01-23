A = int(input())
B = int(input())
C = int(input())

temp = A*B*C

str_temp = str(temp)
length = len(str_temp)


result_hash = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}

for i in range(length):
    ttemp = temp % 10
    result_hash[ttemp] += 1
    temp = temp // 10

for key,value in result_hash.items():
    print(value)
