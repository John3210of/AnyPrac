class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # 이분탐색?
        # 최소힙 2개로 가져가기? 그냥 일단 정렬하고 하는게 나을듯
        def can_finish(piles, h, takes):
            # 아무튼 먹는시간이 h보단 작거나 같아야한다.
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / takes)
            return hours <= h

        low, high = 1, max(piles)
        
        while low < high:
            mid = (low + high) // 2
            if can_finish(piles, h, mid):
                high = mid
            else:
                low = mid + 1
        
        return low
