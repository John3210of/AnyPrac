# https://leetcode.com/problems/climbing-stairs/description/?envType=study-plan-v2&envId=top-interview-150

class Solution:
    def climbStairs(self, n: int) -> int:
        # dp문제 n은 n-1,n-2번째 계단에서 올라오는 경우의 수의합
        dp=[0]*46
        dp[1]=1
        dp[2]=2
        for i in range(3,len(dp)):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]