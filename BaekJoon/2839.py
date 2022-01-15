N = int(input())

result = 0
three_counter = 0
five_counter = 0
if N < 5:
    three_counter = N//3
    if N%3 != 0:
        three_counter = 0
        result = -1
else:
    five_counter = N//5
    if N%5 != 0:
        three_counter += (N%5)//3
        if (N%5)%3 != 0:
            three_counter = 0
            five_counter = 0
            result = -1

print(result+five_counter+three_counter)
    