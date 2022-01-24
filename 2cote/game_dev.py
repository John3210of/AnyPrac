# 4-3 게임개발
# row, col = map(int, input('row,col: ').split())
# sr, sc, sd = map(int, input('start row,col,direction: ').split())
# game_map=[]
# for i in range(row):
# game_map.append(list(map(int,input('mapping: ').split())))
# print(game_map)
# N, M을 공백을 기준으로 구분하여 입력받기
# n, m = map(int, input().split())
# game_map = []
# for i in range(n):
# game_map.append(list(map(int, input().split())))

row = 4
col = 4
game_map = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
# 시작 값

r = 1  # 횡
c = 1  # 종
direction = 0

# 북 동 남 서 0 1 2 3 // -1 => 3
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
game_map[r][c] = 2  # 초기 방문 위치
count = 1
rotate = 0

while True:

    direction -= 1  # 반시계 회전
    if direction == -1:
        direction = 3
    nr = r + dr[direction]
    nc = c + dc[direction]

    # 회전 후 갈 수 있을때
    if game_map[nr][nc] == 0:
        game_map[nr][nc] = 2
        r = nr
        c = nc
        count += 1
        rotate = 0
        print('회전 후 갈수 있을때')
        print('direction: ', direction)
        print('count: ', count)
        print('현재 row,col: ', r, c)
        continue

    else:
        rotate += 1
        print('회전 후 갈 수 없다 loop')
        print('direction: ', direction)

    # 네 방향 모두 갈 수 없는 경우
    if rotate == 4:
        print('네방향 모두 갈수 없는 경우 r, c: ', r, c)
        nr = r - dr[direction]
        nc = c - dc[direction]
        print('네방향 모두 갈수 없는 경우 nr,nc: ', nr, nc)
        print('direction: ', direction)
        # 후진
        if game_map[nr][nc] != 1:
            print('후진할때 nr, nc: ', nr, nc)
            print('후진할때 r, c: ', r, c)
            r = nr
            c = nc

        # 후진시 바다일때
        else:
            break

        rotate = 0

# 정답 출력
print(count)
