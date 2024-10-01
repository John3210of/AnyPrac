class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        idx = 0
        cnt=0
        # while idx < len(nums):
        while cnt < len(nums):
            cnt+=1
            temp = nums[idx]
            for i in range(idx+1,len(nums)):
                if temp + 1 == nums[i]:
                    temp += 1
                else:
                    idx = i-1
                    break
            if temp == nums[idx]:
                result.append(str(temp))
            else:
                result.append(str(nums[idx])+'->'+str(temp))
            print(result)
        return result