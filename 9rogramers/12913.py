#https://school.programmers.co.kr/learn/courses/30/lessons/12913?language=python3 땅따먹기
def get_max_two(lst):
    max1,max2,max1_index,max2_index=0,0,0,0
    for i,v in enumerate(lst):
        if max1 < v:
            max2 = max1
            max2_index = max1_index
            max1 = v
            max1_index = i
        elif max2 < v:
            max2 = v
            max2_index = i
    return [(max1_index,max1),(max2_index,max2)]
    
def solution(land):
    # 현재 열의 정보를 내려주고 
    # 현재행의 최대값2개를 가지고 다음행에 전부 더해서 최대값을 갱신한다.
    # n행까지 진행후에, 마지막행의 max값을 return
    answer = 0
    values=[0,0,0,0]
    while land:
        options = get_max_two(values)
        for i,_ in enumerate(land[-1]):
            if i!=options[0][0]:
                land[-1][i]+=options[0][1]
            else:
                land[-1][i]+=options[1][1]
        values = land.pop()
    answer= max(values)
    return answer