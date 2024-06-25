from collections import deque
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # 그냥 무한대 때리고 갱신하기
        start=float('inf')
        middle=float('inf')
        for num in nums:
            if num < start:
                start=num
            elif start < num < middle:
                middle=num
            elif middle < num:
                return True
        return False


        # 연속된이 애초에 아니었음 ㅇㅇ;
        # 연속된 3개의수가 정렬된 경우라면 true, 아니면 false?
        # queue에 넣으면서 길이가 3이 되는순간 true
        # queue=deque(nums)
        # answer=[]
        # while queue:
        #     number=queue.popleft()
        #     if len(answer)==0:
        #         answer.append(number)
        #     elif answer[-1] < number:
        #         answer.append(number)
        #         if len(answer)==3:
        #             return True
        #     else:
        #         answer=[number]
        # return False