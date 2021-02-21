result_list = []
mul = 0
A = input()
if A == 'black':
    result_list.append('0')
if A == 'brown':
    result_list.append('1')
if A == 'red':
    result_list.append('2')
if A == 'orange':
    result_list.append('3')
if A == 'yellow':
    result_list.append('4')
if A == 'green':
    result_list.append('5')
if A == 'blue':
    result_list.append('6')
if A == 'violet':
    result_list.append('7')
if A == 'grey':
    result_list.append('8')
if A == 'white':
    result_list.append('9')
B = input()
if B == 'black':
    result_list.append('0')
if B == 'brown':
    result_list.append('1')
if B == 'red':
    result_list.append('2')
if B == 'orange':
    result_list.append('3')
if B == 'yellow':
    result_list.append('4')
if B == 'green':
    result_list.append('5')
if B == 'blue':
    result_list.append('6')
if B == 'violet':
    result_list.append('7')
if B == 'grey':
    result_list.append('8')
if B == 'white':
    result_list.append('9')
C = input()

if C == 'black':
    mul = 1
if C == 'brown':
    mul = 10
if C == 'red':
    mul = 100
if C == 'orange':
    mul = 1000
if C == 'yellow':
    mul = 10000
if C == 'green':
    mul = 100000
if C == 'blue':
    mul = 1000000
if C == 'violet':
    mul = 10000000
if C == 'grey':
    mul = 100000000
if C == 'white':
    mul = 1000000000

temp = "".join(result_list)
temp = int(temp)
temp = temp*mul
print(temp)