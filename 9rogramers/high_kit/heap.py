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

# 3.이중우선순위큐
import heapq
def solution(operations):
    # 최대힙과 최소힙 두개를 구해서 각각의 0번 인덱스를 answer로 return
    # python은 기본적으로 최소힙을 지원하므로 max_heap에는 -부호로 넣어주고 꺼내서 -1을 마지막에 곱해준다.
    # heap pop을할시에 최소힙에서는 최소값, 최대힙에서는 최대값이 나온다.
    min_heap=[]
    max_heap=[]
    
    for oper in operations:
        command, num = oper.split()
        num = int(num)
        
        if command == "I":
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        elif command == "D":
            if num == 1:
                if max_heap: 
                    max_val = -heapq.heappop(max_heap)
                    min_heap.remove(max_val)
            elif num == -1:
                if min_heap:
                    min_val = heapq.heappop(min_heap)
                    max_heap.remove(-min_val)
    if not max_heap:
        return [0,0]
    
    return [-heapq.heappop(max_heap),heapq.heappop(min_heap)]