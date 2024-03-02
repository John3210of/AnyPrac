# https://school.programmers.co.kr/learn/courses/30/lessons/138476 귤고르기
from collections import Counter

def solution(k, tangerine):
    dic = Counter(tangerine)
    values = sorted(list(dic.values()),reverse=True)
    temp=0
    answer=0
    for i in range(k):
        temp+=values[i]
        if temp>=k:
            answer=i+1
            break
    return answer


tangerine=[1, 3, 2, 5, 4, 5, 2, 3]
k=6
print(solution(k,tangerine))