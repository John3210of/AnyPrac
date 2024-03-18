# https://school.programmers.co.kr/learn/courses/30/lessons/131704?language=python3 택배상자
def solution(order):
    assistance = []
    answer = 0
    for box in range(1, len(order) + 1):
        if order[answer] != box:
            assistance.append(box)
        else:
            answer += 1
            while assistance and order[answer] == assistance[-1]:
                assistance.pop()
                answer += 1
    return answer
print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))  
