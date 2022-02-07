import sys


N,M = map(int,sys.stdin.readline().split())
reverse_pokemon = {}
pokemon = {}
question = []
for i in range(N):
    tmp = sys.stdin.readline().strip('\n')
    pokemon[tmp] = i+1
    reverse_pokemon[i+1] = tmp
for i in range(M):
    question.append(sys.stdin.readline().strip('\n'))

for i in question:
    if ord('A') <= ord(i[0]) <= ord('Z'):
        print(pokemon[i])
    else:
        print(reverse_pokemon[int(i)])
