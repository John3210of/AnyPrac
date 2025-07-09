def solution(n, times):
    '''
    가능한건지 아닌건지
    
    27분에 6명이 가능한지?
     7 14 21 28
    10 20 30 40 이런식으로 배수를 넣고 중복 가능하게 해서 인덱스의 위치가 n명을 태우는 최소의 수
    '''
    max_time = max(times)*n
    start = 0
    answer = float('inf')
    while start < max_time:
        mid = (start + max_time)//2
        temp = 0
        for time in times:
            temp += mid//time
        if temp >= n:
            answer = min(answer,mid)
            max_time = mid
        else:
            start = mid + 1
    
    return answer