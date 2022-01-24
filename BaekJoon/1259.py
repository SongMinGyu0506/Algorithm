import sys


while True:
    case1 = str(sys.stdin.readline())
    if case1 == '0\n':
        break
    case2 = ''
    for i in reversed(range(len(case1))):
        case2 = case2+case1[i]
    case1 = int(case1)
    case2 = int(case2)
    if case1 == case2:
        print('yes')
    else:
        print('no')
