class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        똑같은데 2개까지만 나오도록
        123455555
        제거를 어케 시켜야하는데
        '''
        pointer = 1
        count = 1
        have_to_remove = []
        '''    
            i=1
               p
            [0,0,1,1,1,1,2,3,3]
                 p
            [0,0,1,1,1,1,2,3,3]
            i=2  p
            [0,0,1,1,1,1,2,3,3]
            i=3  
            [0,0,1,1,1,1,2,3,3]
                   p
            [0,0,1,1,1,1,2,3,3]
            i=4
            [0,0,1,1,1,1,2,3,3]
            [0,0,1,1,1,1,2,3,3]
            [0,0,1,1,1,1,2,3,3]
            [0,0,1,1,1,1,2,3,3]
            [0,0,1,1,1,1,2,3,3]
            [0,0,1,1,1,1,2,3,3]

        '''
        before = nums.count(nums[-1])
        if before == len(nums):
            # EX1
            return 1 if len(nums)==1 else 2
        for i in range(1, len(nums)):
            # 1칸이 겹칠경우
            if nums[i] == nums[i - 1]:
                count += 1
            else:
                count = 1
            # 2개가 같은 경우까지는 허용한다.
            if count <= 2:
                nums[pointer] = nums[i]
                pointer += 1
        after = nums.count(nums[-1])
        for i in range(after-before):
            nums.pop()
        while pointer < len(nums):
            nums.pop()
            pointer += 1
        return len(nums)
'''
EX1
Input
nums =
[1,1,1]
Output
[1,1]
Expected
[1,1]

EX2
Input
nums =
[1,2,2,2]
Output
[1,2,2,2]
Expected
[1,2,2]
'''