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

class Solution:
    # divide and conquer
    # quad-tree를 재귀적으로 만든다.
    # 종료조건은 모든 grid의 값이 같거나 더이상 나누어질 수 없다면
    # Node가 leaf_node로서 반환됨, 여기서 모든 grid의 값이 같다 == 더이상 나누어질 수 없다.
    # 재귀가 종료된뒤, Node를 반환하여 종료한다.
    # quad_tree를 만들때는 grid,row,col,grid_size가 필요하다.
    
    def construct(self, grid: List[List[int]]) -> 'Node':
        return self.construct_quad_tree(grid,0,0,len(grid))
    
    def construct_quad_tree(self,grid,row,col,size):
        if self.is_leaf(grid,row,col,size):
            return Node(grid[row][col],True)    
        next_size = size//2
        top_left = self.construct_quad_tree(grid,row,col,next_size)
        top_right = self.construct_quad_tree(grid,row,col+next_size,next_size)
        bottom_left = self.construct_quad_tree(grid,row+next_size,col,next_size)
        bottom_right = self.construct_quad_tree(grid,row+next_size,col+next_size,next_size)
        return Node(1,False,top_left,top_right,bottom_left,bottom_right)
    
    def is_leaf(self,grid,row,col,size):
        for i in range(row,row+size):
            for j in range(col,col+size):
                if grid[i][j] != grid[row][col]:
                    return False
        return True