from os import GRND_RANDOM


n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

white,blue = 0,0
def sol(y,x,term):
    global white, blue
    color = graph[y][x]
    
    for dy in range(y,y+term):
        for dx in range(x,x+term):
            if color != graph[dy][dx]:
                print('(',end='')
                sol(y,x,term//2)
                sol(y,x+term//2,term//2)
                sol(y+term//2,x,term//2)
                sol(y+term//2,x+term//2,term//2)
                print(')',end='')
                return
    if color == 0:
        print(0,end='')
    elif color == 1:
        print(1,end='')

sol(0,0,n)
print()