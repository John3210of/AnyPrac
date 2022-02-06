# n=int(input())
# k=int(input())
# apple=[]
# for i in range(3):
#     apple.append(list(map(int, input().split())))
# move_switch=[]
# l = int(input())
# for i in range(l):
#     move_switch.append(list(input().split()))
from collections import deque

n = 6
k = 3
apple = [[3, 4], [2, 5], [5, 3]]


move_switch = [['3', 'D'], ['15', 'L'], ['17', 'D']]
for i in range(len(move_switch)):
    int(move_switch[i][0])

graph = [[0] * n for _ in range(n)]

# 초기 뱀의 길이는 1
# 뱀은 처음에 (0,0)에서 우측으로 먼저 이동한다.
# 몸길이를 늘리며 이동한후, 사과가 있다면 몸길이 유지 // 사과가 없다면 몸길이 -1 =>꼬리칸을 지워준다.
# 이동하면서 몸통과 만난다면 게임종료.

# snake 에 좌표위치를 어떻게 저장할지.
# snake=[[0,0],[0,1] >>> 가면서 사과가 없다면 popleft, 있다면 그대로 유지.하고 cnt++ 만약 움직일 좌표가 in snake라면 게임오버.

snake = [[2, 2]]
snake = deque(snake)

# move>>우 하 좌 상
# 움직임을 어떻게 구현할지

d_row = [0, 1, 0, -1]
d_col = [1, 0, -1, 0]
direction = [d_row[0], d_col[0]]
cnt = 0
while True:
    next_point = [snake[-1][0] + direction[0], snake[-1][1] + direction[1]]
    # print('next_point',next_point)
    if next_point in snake or next_point[0] >= n or next_point[1] >= n:  # gameover 조건
        print(cnt)
        break
    snake.append(next_point)
    cnt += 1        # 이동후 시간증가
    # print('next_point in real:',[next_point[0] + 1, next_point[1] + 1])
    if [next_point[0] + 1, next_point[1] + 1] not in apple: # 리스트의 좌표+1 해야 입력해준 실제좌표
        snake.popleft()




