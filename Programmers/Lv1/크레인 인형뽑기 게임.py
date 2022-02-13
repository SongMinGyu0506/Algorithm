from collections import deque

def solution(board, moves):
    answer = 0
    moves = [moves[i]-1 for i in range(len(moves))]
    stack = deque()
    for i in moves:
        for j in range(len(board)):
            if board[len(board)-1][i] == 0:
                break
            if board[j][i] == 0:
                continue
            if len(stack) == 0:
                stack.append(board[j][i])
                board[j][i] = 0
                break
            if stack[-1] == board[j][i]:
                board[j][i] = 0
                stack.pop()
                answer += 2
                break
            else:
                stack.append(board[j][i])
                board[j][i] = 0
                break
    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]
print(solution(board,moves))