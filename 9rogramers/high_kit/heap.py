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

#2. 디스크 컨트롤러
import heapq

def solution(jobs):
    answer, now, i = 0, 0, 0
    start = -1
    heap = []
    # [[0, 3], [1, 9], [2, 6]]
    while i < len(jobs):  # 현재 시점에서 처리할 수 있는 작업을 heap에 저장
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(heap, [j[1], j[0]])
        if len(heap) > 0:  # 처리할 작업이 있는 경우
            cur = heapq.heappop(heap)
            start = now
            now += cur[0]
            answer += now - cur[1]  # 작업 요청시간부터 종료시간까지의 시간 계산
            i += 1
        else:  # 처리할 작업이 없는 경우 다음 시간을 넘어감
            now += 1

    return answer // len(jobs)