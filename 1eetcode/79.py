class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking
        # 종료 조건: word와 string이 일치할 때, 혹은 중간 값이 같지 않을 때
        drow = [1, -1, 0, 0]
        dcol = [0, 0, 1, -1]
        def backtracking(string, row, col, visited):
            if word[:len(string)] != string:
                return False
            if word == string:
                return True
            for i in range(4):
                next_row = row + drow[i]
                next_col = col + dcol[i]
                if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]) and not visited[next_row][next_col]:
                    visited[next_row][next_col] = True
                    if backtracking(string + board[next_row][next_col], next_row, next_col, visited):
                        return True
                    visited[next_row][next_col] = False
            return False
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0]:
                    visited = [[False] * len(board[0]) for _ in range(len(board))]
                    visited[row][col] = True
                    if backtracking(board[row][col], row, col, visited):
                        return True
        return False
    # 시간 복잡도 O(n * m * k) >> O(n*m*4^k)
    # 공간 복잡도 O(n*m + k)