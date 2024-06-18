class Solution:
    def is_vaild_list(self, lst):
        seen = set()
        for num in lst:
            if num != '.':
                if num in seen:
                    return False
                seen.add(num)
        return True

    def is_vaild_width(self, board):
        for row in board:
            if not self.is_vaild_list(row):
                return False
        return True

    def is_vaild_height(self, board):
        for col in range(9):
            if not self.is_vaild_list([board[row][col] for row in range(9)]):
                return False
        return True

    def is_vaild_cube(self, board): 
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_vaild_list(
                    [board[x][y] for x in range(i, i+3) for y in range(j, j+3)]
                ):
                    return False
        return True
    
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if self.is_vaild_width(board) and self.is_vaild_height(board) and self.is_vaild_cube(board):
            return True
        else:
            return False 