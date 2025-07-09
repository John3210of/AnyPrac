import math
def solution(n, stations, w):
    '''
    그리디
    리스트의 길이가 2억이므로 n, logn 수준으로 끝내야함
    
    '''
    answer = 0
    before_end = 1
    for station in stations:
        answer += math.ceil((station - w - before_end)/(2*w+1))
        before_end = station+w+1
    if station + w < n:
        answer += math.ceil((n - (station + w))/(2*w+1))
    
    return answer