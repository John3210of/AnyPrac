from collections import deque
def solution(routes):
    '''
    정렬시켜서 최대한 도착지점에 배치하고 이게 어디까지 영향을 미치는지 확인
    그리고 다시 최대한 마지막에 설치하는 그리디
    '''
    answer = 0
    routes.sort(key = lambda x:x[1])
    queue = deque(routes)
    cctv_point = float('-inf')
    while queue:
        start, end = queue.popleft()
        if start <= cctv_point <= end:
            continue
        else:
            answer += 1
            cctv_point = end
    return answer