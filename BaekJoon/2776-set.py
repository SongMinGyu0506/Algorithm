T = int(input())
for i in range(T):
    N = int(input())
    note1 = list(map(int,input().split(' ')))
    M = int(input())
    note2 = list(map(int,input().split(' ')))
    note1_hash = {}
    for i in note1:
        note1_hash[i] = 1

    for i in note2:
        try:
            print(note1_hash[i])
        except Exception:
            print(0)
    #print(note1_hash[note2[0]])