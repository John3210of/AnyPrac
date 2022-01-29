import sys
from collections import deque

input = sys.stdin.readline
N, M, K, X = map(int, input().split())  # 도시개수,도로개수,최단거리,출발도시의번호
graph = [[] for _ in range(1 + N)]

for i in range(M):  # 도로정보입력받기
    a, b = map(int, input().split())
    graph[a].append(b)  # 1 2 / 1 3 / 2 3 / 2 4  딕셔너리로 하려고 했지만 이방법이 더 쉬운듯.
print(graph)

distance = [-1] * (N + 1)  # 최단거리가 k인 도시가 존재하지 않을경우 -1을 return하므로..
                           # N+1을 하는이유는 idx_num과 도시num 맞추려고
distance[X] = 0

print('distance: ', distance)

q = deque([X])

while q:
    now = q.popleft()
    for next in graph[now]:
        if distance[next] == -1:  # 아직 가지 않았다면
            distance[next] = distance[now] + 1
            q.append(next)  # bfs

flag = 1
for i in range(1, N + 1):
    if distance[i] == K:  # 최단거리가 k인 도시의 번호 출력
        print(i)
        flag = 0

if flag == 1:  # 최단거리가 k가 없다면 print(-1)
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
# #       ## m회 입력. 띄어쓰기로 나누어서 list에 append
#
# # 첫번째 index 가 있는 리스트에 두번째 index가 있다면 n to m = 1
#
#
# # start = lst[x][0]
# # end = lst[x][1] ==> start일 경우에 거리++