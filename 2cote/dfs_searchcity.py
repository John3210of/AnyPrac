from collections import deque
import sys

input = sys.stdin.readline
INF = int(1e9)  # 도시 개수, 도로 개수, 최단 거리, 출발 도시
n, m, k, x = map(int, input().split())  # 각 도시에 연결된 도로 정보를 담는 리스트
graph = [[] for i in range(n + 1)]  # 최단 거리 테이블
distance = [INF] * (n + 1)  # 모든 도로 정보 입력 받기
for _ in range(m):
    i, j = map(int, input().split())
    graph[i].append(j)  # 도시 i에서 도시 j까지 도로가 존재


def solution(start):
    answer = []
    queue = deque([start])
    distance[start] = 0  # bfs 방식으로 인접 도시들 방문
    while queue:
        v = queue.popleft()
        if distance[v] == k:
            answer.append(v)
        if distance[v] > k:  # 나머지 도시들은 최단 거리가 k 이상
            return answer
        for x in graph[v]:  # 현재 도시 v를 거쳐서 도시 x까지 가는게 더 짧은 경우
            if distance[v] + 1 < distance[x]:
                distance[x] = distance[v] + 1
                queue.append(x)

    return answer


answer = solution(x)
if answer:
    answer.sort()
    for x in answer:
        print(x)
else:
    print(-1)

# # 도시의 갯수 N, 도로의 갯수 M,
# # 거리정보 K, 출발 도시의 번호 X
#
# # X로부터 출발하여 도달할 수 있는 도시 중에서, 최단거리가 k인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력합니다.
# # 이때 도달할 수 있는 도시 중에서, 최단 거리가 k인 도시가 하나도 존재하지 않으면 -1을 출력합니다.
# N = 4
# M = 4
# K = 2
# X = 1
# # n, m, k, x = map(int, input().split())
#
# val = [[1, 2], [1, 3], [2, 3], [2, 4]]
# # val = []
# # for i in range(M):
# #     val.append((list(map(int, input().split()))))  ## m회 입력. 띄어쓰기로 나누어서 list에 append
#
# # 첫번째 index 가 있는 리스트에 두번째 index가 있다면 n to m = 1
#
#
# # start = lst[x][0]
# # end = lst[x][1] ==> start일 경우에 거리++
