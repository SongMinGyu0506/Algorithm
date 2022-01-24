N = int(input())
alpha = input()

result = 0
cnt = 0
for i in alpha:
    if ord(i) <= 90:
        result = (result + ((ord(i)-64)*(31**cnt)))%1234567891
    else:
        result = (result + ((ord(i)-96)*(31**cnt)))%1234567891
    cnt += 1
print(result)