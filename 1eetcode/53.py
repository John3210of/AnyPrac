class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 1개짜리, 2개짜리 , ... , len(nums)개 짜리가 아니고
        # 이전까지의 합이 현재 보려는 값보다 작다면 무시하는방식
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(nums[i],nums[i]+dp[i-1])
        return max(dp)