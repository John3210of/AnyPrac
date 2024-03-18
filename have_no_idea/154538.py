# https://school.programmers.co.kr/learn/courses/30/lessons/154538 숫자변환하기
from collections import deque

def solution(x, y, n):
    queue = deque([(x, 0)])  # (현재 숫자, 연산 횟수)
    visited = set()
    while queue:
        current, count = queue.popleft()
        if current == y:
            return count
        if current in visited:
            continue
        visited.add(current)
        if current > y:
            continue
        queue.append((current + n, count + 1))
        queue.append((current * 2, count + 1))
        queue.append((current * 3, count + 1))
    return -1
