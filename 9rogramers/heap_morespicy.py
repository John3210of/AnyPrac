import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    if scoville[0] >= K:
        return 0

    for _ in range(len(scoville) - 1):
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        c = a + 2 * b
        heapq.heappush(scoville, c)
        answer += 1
        if scoville[0] >= K:
            return answer

    return -1
