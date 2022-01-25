# # 음료수 얼려먹기
# # 상하좌우끼리 붙어있는 경우 연결되어 cnt++

# 조건1) 음료수를 얼릴수 있는 노드 전부 cnt++

# 조건2) 얼릴수 있는곳과 인접한 노드 전부 얼릴수 없도록 만들기

iced = [[0, 1, 0, 1, 0],
        [0, 1, 1, 0, 1],
        [1, 0, 1, 0, 1],
        [0, 1, 0, 1, 0]]

# 상 하 좌 우

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# print(len(iced[0]))

def icecream(iced):
    cnt = 0

    def dfs(row, col):

        if iced[row][col] == 1:
            return
        iced[row][col] = 1

        for i in range(4):  # 상하좌우 가야됨
            nr = row + dr[i]
            nc = col + dc[i]
            if nr < 0 or nc < 0 or nr >= 4 or nc >= 5:  # 멈춰
                continue
            dfs(nr, nc)

    for row in range(len(iced)):  # node 갯수 세는법 여길 몰랐다
        for col in range(len(iced[0])):
            node = iced[row][col]
            if node == 0:
                cnt += 1
                dfs(row, col)

    print('cnt: ', cnt)


icecream(iced)


#
#     ##여기까지가 안보고 친거###########

# 음료수 얼려먹기
# 상하좌우끼리 붙어있는 경우 연결되어 cnt++


# def icecream(iced):
#     # 상 하 좌 우
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
#     cnt = 0
#
#     def dfs(row, col):
#
#         if row < 0 or col < 0 or row >= 4 or col >= 5 or iced[row][col] == 1:  # 멈춰
#             return
#
#         iced[row][col] = 1
#
#         for i in range(4):  # 상하좌우 가야됨
#             dfs(row + dr[i], col + dc[i])
#         return
#
#     for row in range(len(iced)):  # node 갯수 세는법
#         for col in range(len(iced[0])):
#             node = iced[row][col]
#             if node == 0:
#                 cnt += 1
#                 dfs(row, col)
#
#     print(cnt)
#     return cnt
#
#
# iced = [[0, 0, 1, 1, 0],
#         [0, 0, 0, 1, 1],
#         [1, 1, 1, 1, 1],
#         [0, 0, 0, 0, 0]]
#
# icecream(iced)
