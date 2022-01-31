#인체에 치명적인 바이러스를 연구하던 연구소에서 바이러스가 유출되었다.

# 다행히 바이러스는 아직 퍼지지 않았고, 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.

# 연구소는 크기가 N×M인 직사각형으로 나타낼 수 있으며, 직사각형은 1×1 크기의 정사각형으로 나누어져 있다.

# 새로 세울 수 있는 벽의 개수는 3개이며, 꼭 3개를 세워야 한다.


# 1을 3개 추가 할 경우에 모든 0으로 부터 시작하는 1을 만날때까지 움직인 횟수를 세는 dfs를 만든다.

# 그중 가장 큰 수를 출력한다.

import copy
from collections import deque

answer = 0

# bfs 탐색
def bfs(answer):
    # 큐 생성 후 그래프와 동일한 모양의 그래프 카피
    q = deque()
    copy_graph = copy.deepcopy(graph)
    # 그래프 돌면서 바이러스인 좌표를 큐에 넣는다
    for i in range(n):
        for j in range(m):
            if copy_graph[i][j] == 2:
                q.append((i, j))

    # 큐가 차있을 때
    while q:
        # 큐에서 꺼내서 x, y 좌표에 넣고
        x, y = q.popleft()
        # 인접 노드로 순회
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 순회할 때 범위 밖이면 다시 돌고
            if nx < 0 or nx >= n or ny < 0 or ny >=m:
                continue
            # 만약에 그래프 값이 0이면(빈칸), 2로 바꿔주고 (바이러스 확산 가능지역), 큐에 다시 넣는다
            if copy_graph[nx][ny] == 0:
                copy_graph[nx][ny]=2
                q.append((nx, ny))

    # 개수 전역변수 선언

    # 안전영역 카운트 변수
    cnt = 0

    # 그래프 돌면서 값이 0이면 카운트
    for i in range(n):
        cnt += copy_graph[i].count(0)

    # 안전영역 카운트 변수와 answer 중에 더 큰 값을 답으로 대치한다
    answer = max(answer, cnt)

    print(answer)

# 벽 만드는 함수
def makeWall(cnt):
        # 벽이 3개 다 세워졌으면
        if cnt == 3:
            # bfs 탐색
            bfs(answer)
            return

        # 그래프 돌면서 (0, 0 ~ n-1, m-1)까지 다 돌아야함 (벽 다 쳐봐서 최대값 구해야되니)
        for i in range(n):
            for j in range(m):
                # 그래프 좌표가 0이면(비었으면)
                if graph[i][j] == 0:
                    # 벽치기
                    graph[i][j] = 1
                    # 벽 개수 올려서
                    makeWall(cnt+1)
                    # 다시 벽 부수기
                    graph[i][j] = 0


n, m = map(int, input().split())
graph = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(n):
    graph.append(list(map(int, input().split())))


makeWall(0)
print(answer)