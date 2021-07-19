n,k = map(int, input().split())

temp_value = n
mid_value = 0
counter = 0
while True:
    if temp_value == 1:
        break
    if temp_value < k:
        counter = counter + (temp_value-1)
        temp_value = temp_value - (temp_value - 1)
        continue
    if temp_value % k == 0:
        temp_value = temp_value / k
        temp_value = int(temp_value)
        counter = counter + 1
        continue
    if temp_value % k != 0:
        counter = counter + (temp_value % k)
        temp_value = temp_value - (temp_value % k)
        continue
print(counter)
