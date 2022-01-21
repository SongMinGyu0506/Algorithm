T = int(input())
for i in range(T):
    N = int(input())
    note1 = list(map(int,input().split(' ')))
    M = int(input())
    note2 = list(map(int,input().split(' ')))
    note2_hash = {}

    for i in note2:
        note2_hash[i] = 0

    note2_tmp = note2
    note1 = sorted(note1)
    #note2 = sorted(note2)

    for note_number in note2:
        mins = 0
        maxs = len(note1)
        while mins < maxs:
            mid = (mins + maxs) // 2
            if note_number == note1[mid]:
                print(1)
                #note2_hash[note_number] += 1
                break
            elif note_number > note1[mid]:
                mins = mid + 1
            elif note_number < note1[mid]: 
                maxs = mid - 1
        if mins >= maxs:
            print(0)
    # for i in note2_tmp:
    #     if note2_hash[i] >= 1:
    #         print(1)
    #     else:
    #         print(0)

