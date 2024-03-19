# https://school.programmers.co.kr/learn/courses/30/lessons/49189 가장먼노드
from collections import deque

def solution(n, vertex):
    # 그래프를 딕셔너리로 선언
    graph = {node: [] for node in range(1, n + 1)}
    distances = {}
    for v in vertex:
        a, b = v
        graph[a].append(b)
        graph[b].append(a)

    for node in range(1, n + 1):
        distances[node] = -1
    distances[1] = 0
    queue = deque([1])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if distances[neighbor] == -1:
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    max_distance = max(distances.values())
    max_keys = [key for key, value in distances.items() if value == max_distance]
    return len(max_keys)

# 예시 입력
n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, vertex))
