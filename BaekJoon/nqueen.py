import sys

n = int(sys.stdin.readline())
board_col = [0 for _ in range(n)]
visited = [False for _ in range(n)]
cnt = 0


def checker(dn):
    for i in range(dn):
        if (board_col[dn] == board_col[i]) or (dn-i == abs(board_col[dn] - board_col[i])):
            return False
    return True

def solution(dn):
    if dn == n:
        global cnt
        cnt += 1
    else:
        for i in range(n):
            board_col[dn] = i
            if checker(dn):
                solution(dn+1)

solution(0)
print(cnt)

