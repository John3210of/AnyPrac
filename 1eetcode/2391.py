import heapq
class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        # 가장 작은값부터 꺼내고 그 수에 count를 곱한값들의 합을 반환
        # 시간복잡도가 문제일듯으로 보인다..인데 조건이 1 <= m == values.length <= 10라서 되는듯
        min_heap = []
        for v in values:
            for s in v:
                heapq.heappush(min_heap,s)
        answer = 0
        for i in range(1,len(min_heap)+1):
            answer += i*heapq.heappop(min_heap)
        return answer
# 시간복잡도 n*mlog(n)
# 공간복잡도 n*m