N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse = True)

temp = 0

for i in range(N):
    temp = temp + (A[i]*B[i])

print(temp)
    