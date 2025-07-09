def solution(n, s):
    '''
    자연수 n개
    1 4 5
    3 3 4
    몫만큼하고 나머지를 뒤에서부터 더하기
    '''
    if n > s:
        return [-1]
    mock = s//n
    leave = s%n
    answer = [mock for _ in range(n)]
    for i in range(len(answer)-1,-1,-1):
        if leave <=0:
            break
        answer[i] += 1
        leave -= 1
        
    return answer