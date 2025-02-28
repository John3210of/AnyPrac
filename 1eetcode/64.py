class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # dp, 할수있는 행동은 오른쪽가기 내려가기
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]
        if len(grid) == 1:
            return sum(grid[0])
        elif len(grid[0]) == 1:
            answer=0
            for i in range(len(grid)):
                answer += sum(grid[i])
            return answer

        for i in range(1,len(grid)):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1,len(grid[0])):
            dp[0][j] = dp[0][j-1] + grid[0][j]

        # r 모양으로 완성해 가는 점화식을 만든다?
        '''
            [
                [1, 4, 5], 
                [2, inf, inf], 
                [6, inf, inf]
            ]
        '''
        for row in range(1,len(grid)):
            for col in range(1,len(grid[0])):
                dp[row][col] = min(dp[row-1][col],dp[row][col-1]) + grid[row][col]
        return dp[-1][-1]
        
   # 시간복잡도 O(m*n), 공간 복잡도 O(m*n)
