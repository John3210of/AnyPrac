# 다익스트라란?

# 출발점이 정해져있을때 다른 노드에 이르기까지의 최소비용
# 출발지를 기준으로 인접노드를 살펴본다.
# 간선에는 비용이 적혀있다.디폴트값은 무한대.
# 이동하고 가장 작은 값으로부터의 비용을 다시 체크한다.

# def dijkstra_naive(graph, start):
#     def get_smallest_node():
#         min_value = INF
#         idx = 0
#         for i in range(1, N):
#             if dist[i] < min_value and not visited[i]:
#                 min_value = dist[i]
#                 idx = i
#         return idx
#
#     N = len(graph)
#     visited = [False] * N
#     dist = [INF] * N
#
#     visited[start] = True
#     dist[start] = 0
#
#     for adj, d in graph[start]:
#         dist[adj] = d
#
#     # N개의 노드 중 첫 노드는 이미 방문했으므로,
#     # N-1번 수행하면 된다.
#     for _ in range(N - 1):
#         # 가장 가깝고 방문 안한 녀석을 고르고,
#         cur = get_smallest_node()
#         visited[cur] = True
#         # 최단거리를 비교, 수정한다.
#         for adj, d in graph[cur]:
#             cost = dist[cur] + d
#             if cost < dist[adj]:
#                 dist[adj] = cost
#
#     return dist

import heapq

INF = int(1e9)

def dijkstra_pq(graph, start):
    N = len(graph)
    dist = [INF] * N

    q = []
    # 튜플일 경우 0번째 요소 기준으로 최소 힙 구조.
    # 첫 번째 방문 누적 비용은 0이다.
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        # 누적 비용이 가장 작은 녀석을 꺼낸다.
        acc, cur = heapq.heappop(q)

        # 이미 답이 될 가망이 없다.
        if dist[cur] < acc:
            continue

        # 인접 노드를 차례대로 살펴보며 거리를 업데이트한다.
        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist

import sys

with open('testcase1.txt') as f:
    sys.stdin = f
    input = sys.stdin.readline
    n, m = map(int, input().split())
    start = int(input())
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append([b, c])