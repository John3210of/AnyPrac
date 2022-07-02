def solution(participant, completion):
    d={}
    for x in participant:
        d[x] = d.get(x,0)+1
    for x in completion:
        d[x] -= 1

    answer = ''
    for key,val in d.items():
        if val > 0:
            answer=key

    return answer