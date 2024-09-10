# 각 노드끼리의 최단거리를 구하는 알고리즘
# 탐색을 진행함에 따라 정점 사이의 경로를 업데이트 하는 DP방식
'''
출발-경유-시작 의 모든 경우를 찾으므로 시간 복잡도는 O(n^3)
공간 복잡도는 O(n^2)

2차원 행렬을 갱신하며 진행된다.
자기 자신은 0, 바로 이동 가능한 경우는 a, 바로 이동이 불가능한 경우 inf 인상태로 초기화해준다.

시작점을 start, 경유지를 middle, 도착지를 end라고 생각하고 값을 갱신한다.
D_start_end = min(D_start_end, D_start_middle + D_middel_end)

이때, 경유지를 기준으로 start-end에 관한 for loop을 선언한다.
'''

# pseudo code
"""
Input : n 개의 정점을 가진 그래프 graph와 각 간선의 가중치가 담긴 2차원 배열 dist[][]
Output : 각 정점 사이의 최단 거리가 갱신된 graph


1. 모든 정점에 대해 초기화한다. 자신은 0, 간선이 존재하면 갱신, 존재하지 않으면 무한대
FOR ALL NODES_START as i:
    FOR ALL NODES_END as j:
        IF i==j: # 자기 자신일 경우
            dist[i][j]=0
        ELSE IF graph(i,j) # 한번에 간선이 존재할 경우
            dist[i][j] = k
        ELSE: # 간선이 존재 하지 않는 경우
            dist[i][j] = 1e9 

2. 경유지 middle을 거쳐, 최단경로를 갱신
FOR ALL NODES_MIDDLE:
    FOR ALL NODES_START:
        FOR ALL NODES_END:
            dist[start][end] = MIN(dist[start][end], dist[start][middle]+dist[middle][end])

3. 갱신된 최단거리 배열 dist
RETURN dist
"""

# 예제 https://www.acmicpc.net/problem/11404
import sys
n=int(sys.stdin.readline())
m=int(sys.stdin.readline())

graph=[[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i==j:
            graph[i][j]=0
for _ in range(m):
    start,end,cost=map(int,sys.stdin.readline().split())
    graph[start-1][end-1]=min(cost,graph[start-1][end-1])
for middle in range(n):
    for start in range(n):
        for end in range(n):
            graph[start][end] = min(graph[start][end],graph[start][middle]+graph[middle][end])
for i in range(n):
    for j in range(n):
        if graph[i][j]==float('inf'):
            print('0',end=' ')
        else:
            print(graph[i][j], end=' ')
    print()