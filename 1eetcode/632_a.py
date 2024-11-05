from typing import List
import heapq


class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 각리스트에서 최소값들을 꺼내고 최소, 최대를 구한다.
        # Merge K sorted Lists + Minimum Sliding Window
        # 1. 각 0번중에 최소, 최대값을 구한다
        # 2. 그 값을 저장한다. 최소값은 리스트에서 뺀다.
        # 3. 1~2를 반복하여 리스트 한개가 빌때, 범위의 최소값을 return
        # 시간복잡도를 위해 k개의 리스트를 병합해서 heap을 사용한다면
        # 리스트의 빈곳을 어떻게 찾을건지

        # 각 0번을 최초에 비교하며, 최소 최대 pq를 만든다.
        # 시간복잡도 개선을 위해 heap에 튜플형태로 저장한다.
        # (nums[i][0], i, 0) 형태로 저장할때, 어느 위치의 리스트의 몇번째 값을 꺼낼지
        # 몇번째를 지정하지 않고 하려 하면 다음과 같은 T.C에 걸린다.
        """
        Wrong Answer
        84 / 93 testcases passed

        Editorial
        Input
        nums =
        [[10],[11]]

        Use Testcase
        Output
        [10,10]
        Expected
        [10,11]
        """
        heap = []
        min_val, max_val = float("inf"), float("-inf")
        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            max_val = max(nums[i][0], max_val)
        answer = [max_val, min_val]
        while heap:
            min_val, nums_index, atom_index = heapq.heappop(heap)
            if max_val - min_val < answer[1] - answer[0]:
                answer = [min_val, max_val]
            if atom_index + 1 < len(nums[nums_index]):
                next_val = nums[nums_index][atom_index + 1]
                heapq.heappush(heap, (next_val, nums_index, atom_index + 1))
                max_val = max(max_val, next_val)
            else:
                break
        return answer
