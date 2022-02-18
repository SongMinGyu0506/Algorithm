import math
import sys

# math.gcd 이용하여 해결하는 방법
def lcm(a,b):
    return (a*b) // math.gcd(a,b)
A,B = map(int,sys.stdin.readline().split())
print(math.gcd(A,B))
print(lcm(A,B))

# 전체 구현

#역순으로 탐색(최대 수 탐색), 둘다 0으로 떨어지는게 최대 공약수
for i in range(min(A,B),0,-1):
    if A%i == 0 and B%i == 0:
        print(i)
        break


#A,B의 최소 배수를 찾는 것
for i in range(max(A,B),(A*B)+1):
    if i%A == 0 and i%B == 0:
        print(i)
        break

# 유클리드 호제법
# x와 y의 최대 공약수 == y와 r의 최대 공약수
#   x    y      r
#   10 % 12 == 10
#   12 % 10 == 2
#   10 % 2 == 0
def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x

# xy를 최대 공약수로 나누면 최소공배수
def LCM(x,y):
    result = (x*y)//GCD(x,y)
    return result