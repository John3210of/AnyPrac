import heapq
def solution(A, B):
    '''
    그리디?
    1 1 2 3 4 5 7 9 
    1 2 3 4 5 6 7 8
    2 3 4 5 6 7 8
    지는 구간
    최소힙으로 
    '''
    answer = 0
    heapq.heapify(A)
    heapq.heapify(B)
    while B:
        a, b = heapq.heappop(A), heapq.heappop(B)
        if b > a:
            answer += 1
        else:
            heapq.heappush(A,a)
        
    return answer