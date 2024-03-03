# https://school.programmers.co.kr/learn/courses/30/lessons/42747 H-indx
def solution(citations):
    # h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용된 h중에 최대값
    # list = [0, 1, 3, 5, 6]
    # 0번이상 인용된 논문 5, 나머지0 조건충족 temp=0
    # 1번이상 인용된 논문 4, 나머지1 조건충족 temp=1
    # 2번이상 인용된 논문 3, 나머지2 조건충족 temp=2
    # 3번이상 인용된 논문 3, 나머지2 조건충족 temp=3
    # 4번이상 인용된 논문 2, 나머지3 조건불충족
    citations.sort()
    temp=0
    for i in range(10001):
        for j in range(len(citations)):
            if i <= citations[j] and len(citations[j:])>=i and len(citations[:j]) <=i:
                temp=i

    return temp