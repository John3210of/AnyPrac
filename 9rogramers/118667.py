# https://school.programmers.co.kr/learn/courses/30/lessons/118667?language=python3 두큐합같게만들기
from collections import deque

def solution(queue1, queue2):
    answer = 0
    target_sum = (sum(queue1) + sum(queue2)) // 2
    queue1_sum = sum(queue1)
    queue1,queue2 = deque(queue1), deque(queue2)
    while queue1 and queue2:
        if queue1_sum < target_sum:
            tmp = queue2.popleft()
            queue1_sum += tmp
            queue1.append(tmp)
            answer += 1
        elif queue1_sum > target_sum:
            queue1_sum -= queue1.popleft()
            answer += 1
        else:
            return answer
    return -1