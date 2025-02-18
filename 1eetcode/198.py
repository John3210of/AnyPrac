class Solution:
    def rob(self, nums: List[int]) -> int:
        # 연속한곳은 털 수 없다.
        # 2칸 이상을 움직여야 한다.
        # dp문제 : 가장 큰것을 저장하기 점화식
        if len(nums) < 2:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0],nums[1])
        elif len(nums) == 3:
            return max(nums[0]+nums[2],nums[1])

        dp=[0 for _ in range(len(nums))]
        dp[0], dp[1] = nums[0], nums[1]
        dp[2] = dp[0] + nums[2]
        # dp[3] = max(dp[0] + nums[3], dp[1] + nums[3])
        dp[3] = max(dp[0],dp[1])+nums[3]
        # dp[n] = max(dp[n-3],dp[n-2]) + nums[n]
        for n in range(4,len(nums)):
            dp[n] = max(dp[n-3],dp[n-2]) + nums[n]
        return max(dp[-1],dp[-2])
