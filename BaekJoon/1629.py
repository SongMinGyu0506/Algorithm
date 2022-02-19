import sys


n = int(input())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]


m,z,o = 0,0,0
def sol(y,x,term):
    global m,z,o
    this_color = graph[y][x]
    for dy in range(y,y+term):
        for dx in range(x,x+term):
            if this_color != graph[dy][dx]:
                sol(y+term//3*0,x+term//3*0,term//3)
                sol(y+term//3*0,x+term//3*1,term//3)
                sol(y+term//3*0,x+term//3*2,term//3)

                sol(y+term//3*1,x+term//3*0,term//3)
                sol(y+term//3*1,x+term//3*1,term//3)
                sol(y+term//3*1,x+term//3*2,term//3)

                sol(y+term//3*2,x+term//3*0,term//3)
                sol(y+term//3*2,x+term//3*1,term//3)
                sol(y+term//3*2,x+term//3*2,term//3)
                return
    if this_color == -1:
        m+=1
    elif this_color == 0:
        z+=1
    else:
        o+=1

sol(0,0,n)

print(m)
print(z)
print(o)