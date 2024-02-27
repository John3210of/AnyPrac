# https://school.programmers.co.kr/learn/courses/30/lessons/42885
def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    start, end = 0,len(people)-1
    while True:
        p1=people[start]
        p2=people[end]
        if p1+p2 <= limit:
            end-=1
        start+=1
        answer+=1
        if start >= end:
            break
    if start==end:
        answer+=1
    return answer