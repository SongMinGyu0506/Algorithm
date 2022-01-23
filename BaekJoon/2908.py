A,B = map(int,input().split())


temp1 = 0
temp2 = 0
temp1 = temp1+(A%10)*100
A=A//10
temp1 = temp1 + (A%10)*10
A=A//10
temp1 = temp1+(A%10)

temp2=temp2+(B%10)*100
B=B//10
temp2=temp2+(B%10)*10
B=B//10
temp2=temp2+(B%10)


print(max(temp1,temp2))