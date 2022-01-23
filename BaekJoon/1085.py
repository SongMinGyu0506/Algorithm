x,y,w,h = map(int,input().split())

result = []

result.append(x-0)
result.append(w-x)
result.append(y-0)
result.append(h-y)

print(min(result))