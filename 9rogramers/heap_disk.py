import heapq
# from bisect import bisect


# 따로 한번 봐라

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


jobs = [[0, 3], [1, 9], [2, 6]]

solution(jobs)




# from collections import deque
#
# jobs = [[0, 3], [1, 9], [2, 6]]
# # [input_time, runtime]
# queue = deque(jobs)
# # 하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다.
# wait=0
# time = queue[0][1]
# while True:
#     # 현재시간에 runtime을 더하고 popleft
#     queue.popleft()
#     if len(queue) <1:
#         break
#     if queue[0][0] > time:  # 일이 중복된 적이 없는 경우
#         time = queue[0][0] + queue[0][1]
#     else:  # 일이 중복되어 들어온 경우
#         time=time+queue[0][1]
#
# print('time: ',time)
#
# # 작업의 요청부터 종료까지 걸린 시간
# # [time+length]
