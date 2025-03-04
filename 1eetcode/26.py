class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        투포인터로 in place를 어케함?
        모르겠다 걍 원소의 갯수 set으로 세고 while박자 ㅇㅇ        
        '''
        nums_set = set(nums)
        for i in range(len(nums_set)):
            val = nums[i]
            while val in nums[i+1:]:
                nums.remove(val)
        return len(nums)

