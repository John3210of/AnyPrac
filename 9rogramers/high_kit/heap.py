import heapq
#1. 더 맵게
def solution(scoville, K):
    answer = 0
    scoville.sort()
    if scoville[0]>=K:
        return 0
    while len(scoville) >= 2:
        temp = heapq.heappop(scoville)
        temp2 = heapq.heappop(scoville)
        heapq.heappush(scoville,temp+temp2*2)
        answer+=1
        if scoville[0] >= K:
            return answer
    return -1