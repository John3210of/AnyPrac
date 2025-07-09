import heapq
def solution(jobs):
    '''
    1. 현재 시간에 처리할 수 있는 jobs들을 모두 queue에서 꺼낸다. 이때, jobs이 없다면 할일을 마친다.
    2. queue가 존재한다면, 소요시간이 작은것을 먼저 처리한다. 이때, 대기한시간 + 소요되는 시간을 반환한다.
    3. jobs는 존재하지만 현재 시간에 처리할 수 없다면, jobs[0][0]을 현재 시간으로 치환한다.
    '''
    heapq.heapify(jobs)
    time = jobs[0][0]
    queue = []
    works = len(jobs)
    answer = []
    while len(answer) < works:
        while jobs: 
            if jobs[0][0] <= time:
                start_time, spend_time = heapq.heappop(jobs)
                heapq.heappush(queue,[spend_time,start_time])
            elif len(queue) == 0 and jobs[0][0] > time:
                time = jobs[0][0]
            else:
                break
        if queue:
            spend_time, start = heapq.heappop(queue)
            time += spend_time
            answer.append(time-start)
    return sum(answer)//works
