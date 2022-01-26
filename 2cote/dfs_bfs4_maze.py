# 이코테 152p 미로탈출

# N x M 미로에 갇혀있고, 괴물이 있는 부분은 0으로, 없는 부분은 1로 되어있다. 출구는 (N-1,M-1), 위치는 (0,0)
# 최소 밟는 타일의 수?
# visited = [[0 for col in range(len(maze[0]))] for row in range(len(maze))]  #visited 초기화

# 이동을 최대한 복잡하게 하지 않는것이 중요함 down과 right를 최우선으로 이동, up과 left는 d와 r이 불가능할때

# case1) ==> maze[][]==0 or 2 ==> maze[][]%2 != 1

# 로직1) 출발한곳 value=2 해줌.
# 로직2) 출발한곳 기준으로 우 하를 먼저 탐색후 갈수있다면 maze[][]=2를 넣어줌
#       case1)의경우 좌상으로감. case1)이 아닐경우 다시 로직2 반복
# 로직3) 리스트 원소가 2인 갯수를 count 해준다. or ## 이 방법 먼저 maze[][]=2 의 바로 밑에 cnt++를 해준다.

# maze = [
#     [1, 1, 1, 0, 1, 0],
#     [0, 1, 0, 1, 1, 1],
#     [1, 1, 0, 0, 0, 1],
#     [1, 0, 1, 1, 1, 1],
#     [1, 1, 1, 0, 1, 1]
# ]
# # 우 하 좌 상
# dr = [0, 1, 0, -1]  # row 수직
# dc = [1, 0, -1, 0]  # col 수평
#
# cnt = 0
#
# def escape_maze(maze):
#
#     def dfs(row, col):
#
#         maze[row][col] = 2
#
#         for i in range(2):
#             nr = row + dr[i]
#             nc = col + dc[i]
#             if maze[nr][nc]==1:  # 우하 기준 갈곳이 있을때
#
#                 dfs(nr, nc)
#             else:
#                 continue
#             # elif maze[nr][nc] == 0 or maze[nr][nc] == 2:
#             #     print('괴물이 있어')
#
#
#         return maze
#     dfs(0,0)
#     print(maze)
#
# ##
# print(maze)
# print('*' * 30)
# escape_maze(maze)

######################### 답지 ##############################
from collections import deque

# N, M을 공백을 기준으로 구분하여 입력 받기
# n, m = map(int, input().split())
n=5
m=6

# 2차원 리스트의 맵 정보 입력 받기

graph = [
    [1, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]
]
# for i in range(n):
#     graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복하기
    while queue:
        print('queue: ', queue)
        x, y = queue.popleft()
        print('after pop.queue: ', queue)
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                print('nx,ny: ',nx,ny)
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    print(graph)
    return graph[n - 1][m - 1]

# BFS를 수행한 결과 출력
print(bfs(0, 0))
