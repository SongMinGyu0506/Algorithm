size = int(input())
x = 1
y = 1
data = input().split()

for i in data:
    if i == 'L':
        if x == 1:
            continue
        else:
            x -= 1
    if i == 'R':
        if x == size:
            continue
        else:
            x += 1
    if i == 'U':
        if y == 1:
            continue
        else:
            y -= 1
    if i == 'D':
        if y == size:
            continue
        else:
            y += 1

print(y,x)