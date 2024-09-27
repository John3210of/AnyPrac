import heapq
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # TC o(n), SC o(1) ???
        # gte n/2 times.. 
        # sort > n log n ..
        # iterate , cnt++, if cnt > len(nums)//2
        # heapify??? heappop spends nlog n...
        # heapq.heapify(nums)
        # cur = heapq.heappop(nums)
        # cnt = 1
        # target = len(nums)//2
        # while cnt <= target:
        #     now = heapq.heappop(nums)
        #     if cur == now:
        #         cnt += 1
        #     else:
        #         cur = now
        #         cnt = 1
        # return cur
        count=0
        cur = ''
        for num in nums:
            if count == 0:
                cur = num
            if cur == num:
                count += 1
            else:
                count -= 1
        return cur