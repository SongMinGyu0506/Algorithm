import sys
require, brands = map(int,sys.stdin.readline().split())
set_lines = []
lines = []
for brand in range(brands):
    set_line, line = map(int,sys.stdin.readline().split())
    set_lines.append(set_line)
    lines.append(line)

result = 0
while require != 0:
    if require >= 6:
        result += min(min(set_lines),6*min(lines))
        require -= 6
    else:
        result += min(min(set_lines),require*min(lines))
        require -= require

print(result)