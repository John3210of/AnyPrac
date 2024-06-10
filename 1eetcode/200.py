class Solution:
    def dfs(self,row,col,grid,visited):
        drow=[-1,1,0,0]
        dcol=[0,0,-1,1]
        visited[row][col]=True
        for i in range(4):
            next_row=row+drow[i]
            next_col=col+dcol[i]
            if 0<=next_row<len(grid) and 0<=next_col<len(grid[0]) and visited[next_row][next_col] is False and grid[next_row][next_col]=='1':
                self.dfs(next_row,next_col,grid,visited)

    def numIslands(self, grid: List[List[str]]) -> int:
        # 덩어리가 몇개인지 dfs 간단구현
        size=0
        visited=[[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visited[row][col] is False and grid[row][col]=='1':
                    self.dfs(row,col,grid,visited)
                    size+=1
        return size