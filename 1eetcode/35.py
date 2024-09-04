class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # log n이면 이분탐색?
        # 반환하는경우는 
        # 1. 정확히 일치하는 경우
        # 2. nums[n-1] < target < nums[n]
        start = 0 
        end = len(nums)-1
        mid=0
        if nums[-1] < target:
            return len(nums)
        elif nums[0] > target:
            return 0
            
        while True:
            mid = (start+end)//2
            if nums[mid-1] < target < nums[mid] or nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid