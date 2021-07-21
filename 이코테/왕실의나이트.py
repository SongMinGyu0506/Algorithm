input_data = input()
row = ord(input_data[0])-ord('a')+1
colum = int(input_data[1])

#print(chr(ord(row)+1))
#print(ord(row)-ord('a')+1)

move = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(-1,2),(1,-2),(1,2)]

count = 0
for step in move:
    temp_row = step[0]+row
    temp_colum = step[1]+colum
    if temp_row > 0 and temp_row < 9 and temp_colum > 0 and temp_colum < 9:
        count += 1

print(count)