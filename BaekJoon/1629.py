A,B,C = map(int,input().split())

def sol(A,B):
    if B == 1:
        return A%C
    else:
        temp = sol(A,B//2)
        if B%2 == 0:
            return temp**2%C
        else:
            return temp**2 * A%C


print(sol(A,B))
