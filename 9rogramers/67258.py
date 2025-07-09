def solution(gems):
    '''
    gems set
    구간 set 이 gems set이 되는 것 중에 가장 작은것
    10^10 투포인터
    각 보석이 존재하는 인덱스를 모두 구한다.
    인덱스중에 가장 큰값이 가장 작은거 ~ 가장 작은값이 가장 큰거
    n^2 안하고 멀로풀지
    
    가장 작은값과 가장 큰값을 기준으로 줄여나가면?
    dia : 1,4,5,8
    ruby : 2,3
    emerald : 6
    sapphire : 7
    ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
    '''
    gem_dict = {}
    for i in range(len(gems)):
        if gems[i] not in gem_dict:
            gem_dict[gems[i]] = [i+1]
        else:
            gem_dict[gems[i]].append(i+1)
    answer = []
    for i in range(len(gems)-1):
        for j in range(i,len(gems)):
            if set(gem_dict.keys()) == set(gems[i:j+1]):
                answer.append([i,j])
    answer.sort(key=lambda x:x[1]-x[0])
    return [answer[0][0]+1,answer[0][1]+1]