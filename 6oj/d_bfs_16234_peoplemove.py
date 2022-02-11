# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
# 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동을 시작한다.
# 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라고 한다.
# 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 편의상 소수점은 버린다.
# 연합을 해체하고, 모든 국경선을 닫는다.


# 1. 0,0 부터 n,n 까지 상하좌우를 비교하는 bfs를 돌린다.
# 2. 만약 조건에 맞는다면 연합된 국가끼리 값을 똑같이 분배하고, cnt++, 다시 bfs를 돌린다.
# 3. 결국 bfs를 돌렸을때 cnt++이 되지 않는다면, cnt를 return한다.

from collections import deque

n, l, r = map(int, input().split())
popularity = [list(map(int, input().split())) for _ in range(n)]
day = 0
graph = dict()


def check(value, input, x, y):  # 인구 이동 조건 확인
    if (input >= l) and (input <= r):
        value.append((x, y))


def border(i, j):
    value = []
    if i - 1 >= 0:
        top = abs(popularity[i - 1][j] - popularity[i][j])
        check(value, top, i - 1, j)
    if i + 1 < n:
        bottom = abs(popularity[i + 1][j] - popularity[i][j])
        check(value, bottom, i + 1, j)
    if j - 1 >= 0:
        left = abs(popularity[i][j - 1] - popularity[i][j])
        check(value, left, i, j - 1)
    if j + 1 < n:
        right = abs(popularity[i][j + 1] - popularity[i][j])
        check(value, right, i, j + 1)
    if value:
        graph[(i, j)] = value


def bfs(start):
    visit = list()
    queue = deque()
    queue.append(start)
    while queue:
        enqueue = queue.popleft()
        if enqueue not in visit:
            visit.append(enqueue)
            queue.extend(graph[enqueue])
    return visit


while True:
    # 인접 그래프 그리기
    for i in range(n):
        for j in range(n):
            border(i, j)

    # 종료 조건
    if not graph:
        break

    # 인구 이동
    while graph:
        movement = bfs(list(graph.keys())[0])
        sum = 0
        # 연합 인구수 조정
        for move in movement:
            sum += popularity[move[0]][move[1]]
        result = int(sum / len(movement))
        for move in movement:
            popularity[move[0]][move[1]] = result
            del (graph[move])  # 연합 해체
    day += 1

print(day)

# from collections import deque
#
# N, L, R = map(int, input().split())
# # N = nxn행렬을 만들겠다.
# # L,R= 인접 국가간의 최소,최대차
# poplation = []
# for i in range(N):
#     poplation.append(list(map(int, input().split())))
#
# union=[]
#
# cnt = 0
#
#
#
# def bfs(row, col):
#     q = deque()
#     q.append((row, col))
#
#     d_row = [-1, 1, 0, 0]   #상하좌우
#     d_col = [0, 0, -1, 1]
#     for i in range(4):
#         if
