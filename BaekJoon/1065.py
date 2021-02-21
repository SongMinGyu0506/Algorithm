N=int(input())
result = 0
hundred = 0
ten = 0
one = 0
counter = 0
start = 0

while True:
    if start == N+1:
        break;
    if start < 100:
        counter = start
        start=start+1
    else:
        temp = start
        hundred = temp//100
        temp = temp%100
        ten = temp//10
        one = temp%10

        if((hundred - ten) == (ten - one)):
            counter=counter+1
        start=start+1
print(counter)