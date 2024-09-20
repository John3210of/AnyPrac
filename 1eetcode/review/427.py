"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
# 시간 복잡도: O(n^2 log n)
# 공간 복잡도: O(n^2)
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        # 하나라도 [0][0]과 다르다면 나누어야함
        # 모두 일치하면 덩어리 채로 필요 없고 덩어리가 node가 val,isLeaf true
        # 길이의 절반까지를 탐색시킴
        return self.quad_tree(grid,0,len(grid),0,len(grid[0]))

    def quad_tree(self,grid,row_start,row_end,col_start,col_end):
        if self.is_leaf(grid,row_start,row_end,col_start,col_end):
            return Node(grid[row_start][col_start],True)
        mid_row = (row_start + row_end) // 2
        mid_col = (col_start + col_end) // 2
        
        top_left = self.quad_tree(grid, row_start, mid_row, col_start, mid_col)
        top_right = self.quad_tree(grid, row_start, mid_row, mid_col, col_end)
        bot_left = self.quad_tree(grid, mid_row, row_end, col_start, mid_col)
        bot_right = self.quad_tree(grid, mid_row, row_end, mid_col, col_end)
        return Node(1,False,top_left,top_right,bot_left,bot_right)
        
    def is_leaf(self,grid,row_start,row_end,col_start,col_end):
        for row in range(row_start,row_end):
            for col in range(col_start,col_end):
                if grid[row_start][col_start] != grid[row][col]:
                    return False
        return True
                        