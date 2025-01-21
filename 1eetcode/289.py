class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        sub = [[0 for _ in range(len(board[0]))] for _ in range(len(board))]
        drow_col = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

        for row in range(len(board)):
            for col in range(len(board[0])):
                val = board[row][col]
                temp = 0

                for i in range(8):
                    next_row = row + drow_col[i][0]
                    next_col = col + drow_col[i][1]
                    if 0 <= next_row < len(board) and 0 <= next_col < len(board[0]):
                        if board[next_row][next_col] == 1:
                            temp += 1

                if val == 1:
                    if temp < 2 or temp > 3:
                        sub[row][col] = 0
                    else:
                        sub[row][col] = 1
                else:
                    if temp == 3:
                        sub[row][col] = 1

        for row in range(len(board)):
            for col in range(len(board[0])):
                board[row][col] = sub[row][col]
