import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # 각리스트에서 최소값들을 꺼내고 최소, 최대를 구한다.
        # 최최소를 삭제하면서 반복한다.
        # 반복은 어느 하나의 리스트라도 빌때까지
        # 범위가 가장 작으면서 값도 가장 작은 값을 리턴한다.
        answer = []
        while True:
            temp_list = []
            min_pair = [None, float('inf')]
            max_pair = [None, float('-inf')]

            for i,n in enumerate(nums):
                n_min = heapq.heappop(n)
                temp_list.append([i,n_min])
                heapq.heappush(n,n_min)

            for index, value in temp_list:
                if value < min_pair[1]:
                    min_pair = [index, value]
                if value > max_pair[1]:
                    max_pair = [index, value]
            heapq.heappop(nums[min_pair[0]])
            answer.append([min_pair[1],max_pair[1]])
            if not nums[min_pair[0]]:
                break
        diff = float('inf')
        for i,v in enumerate(answer):
            if v[1]-v[0] < diff:
                diff = v[1]-v[0]
                answer_idx = i
        return answer[answer_idx]
    # 이렇게하면 시간초과남 시간복잡도 n^2 log(n) ?