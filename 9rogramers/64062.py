from collections import deque

def solution(stones, k):
    '''
    슬라이딩 윈도우 단조 감소 큐
    임의의 큐 queue는 arr의 인덱스를 가지는데, 가장 큰 인덱스를 queue[0]에 가지도록 한다.
    윈도우 범위까지 커졌다면, 그때부터 최대값을 임의의 리스트 result에 저장한다.
    '''
    queue = deque()
    result = []
    for i in range(len(stones)):
        while queue and stones[queue[-1]] <= stones[i]:
            queue.pop()
        queue.append(i)
        if queue[0] < i-k+1:
            queue.popleft()
        if i >= k-1:
            result.append(stones[queue[0]])
    return min(result)
