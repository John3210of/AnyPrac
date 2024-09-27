from collections import deque
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        queue=deque()
        for i in range(len(nums)):
            queue.append(nums.pop())
        count=0
        for i in range(len(queue)):
            temp = queue.popleft()
            if temp == val:
                count+=1
            else:
                nums.append(temp)
        for i in range(count):
            nums.append('_')
        return len(nums)-count