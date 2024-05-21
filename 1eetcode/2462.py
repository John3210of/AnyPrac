import heapq
from collections import deque
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        '''
        priority queue?
        앞으로 c, 뒤로 c개의 2개의 리스트에서 가장 작은값인데, 겹치면 인덱스가 더 작은값
        c * 2 >= len(costs)라면, middle은 존재하지 않음
        
        앞에서빼는지 뒤에서빼는지에 대한 판단이 필요함 계속 min을 쓰는것도 너무 비효율적일것 같은데
        heapq에서 뺄때, index에 대한 정보를 어떻게 얻지 > 사실은 필요 없음
        어차피 heap화 해도 탄착군이 바뀌지 않으므로
        
        추가해야할 논리는 겹칠때에, 어떻게 할것인가=> 겹친다는건 애초에 사이즈가 작다는뜻인데
        '''
        size=len(costs)
        hired=0
        flag=False
        
        if candidates*2 >= size:
            heapq.heapify(costs)
            for _ in range(k):
                hired+=heapq.heappop(costs)
            return hired

        left=costs[:candidates]
        middle=deque(costs[candidates:-candidates])
        right=costs[-candidates:]
        heapq.heapify(left)
        heapq.heapify(right)
        
        for _ in range(k):
            if candidates*2 >= size:
                if not flag:
                    flag=True
                    costs=left+right
                    heapq.heapify(costs)
                hired += heapq.heappop(costs)
            else:
                if left[0]<=right[0]:
                    hired+=heapq.heappop(left)
                    heapq.heappush(left,middle.popleft())
                else:
                    hired+=heapq.heappop(right)
                    heapq.heappush(right,middle.pop())
                size-=1
        return hired