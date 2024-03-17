# https://school.programmers.co.kr/learn/courses/30/lessons/132265 롤케이크자르기
from collections import defaultdict

def solution(topping):
    answer = 0
    a = defaultdict(int)
    b = defaultdict(int)
    for top in topping:
        b[top] += 1  # 두 번째 조각에서의 각 토핑의 등장 횟수 계산
    for top in topping:
        b[top] -= 1
        a[top] += 1
        if b[top] == 0:
            del b[top]
        if len(a) == len(b):
            answer += 1
    return answer


print(solution(["1", "2", "1", "3", "1", "4", "1", "2"]))

