# https://school.programmers.co.kr/learn/courses/30/lessons/17679 프렌즈4블록
def solution(m, n, board):
    board = [list(row) for row in board]
    while True:
        removed = set()
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i][j + 1] == board[i + 1][j] == board[i + 1][j + 1] != '.':
                    removed |= {(i, j), (i, j + 1), (i + 1, j), (i + 1, j + 1)}
        for i, j in removed:
            board[i][j] = '.'
        if not removed:
            break

        for j in range(n):
            for i in range(m - 1, 0, -1):
                if board[i][j] == '.':
                    for k in range(i - 1, -1, -1):
                        if board[k][j] != '.':
                            board[i][j], board[k][j] = board[k][j], board[i][j]
                            break
    return sum(row.count('.') for row in board)