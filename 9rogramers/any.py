dirs = list('UUUUU')
from collections import deque

def solution(dirs):

    q = deque(dirs)
    x, y = 5, 5
    start = [x, y]  # 시작점(현재위치한 좌표)
    visited = []  # 이동한 좌표

    dx = [0, 0, -1, 1] #col
    dy = [-1, 1, 0, 0] #row
    move_types = ["L", "R", "U", "D"]

    while q:  # dirs의 길이만큼 반복
        print('HI im while')
        direction = q.popleft()  # 첫번째 움직일 방향을 추출
        print('direction',direction)
        for i in range(len(move_types)):  # move_types의 횟수만큼 반복하면서
            if direction == move_types[i]:  # direction이 move_types와 일치할때 새로운 좌표값을 줌
                print('move',move_types[i])
                x = x + dx[i]
                y = y + dy[i]
                nstart = [x, y]
                print('start: ', start)
                print('nstart: ',nstart)
                if x < 0 or x >= 11 or y < 0 or y >= 11:
                    continue

                visited.append([start, nstart])
                visited.append([nstart, start])

                start = nstart

    print('visited:', visited)
    print('cnt: ',int(len(visited)/2))
    return int(len(visited)/2)


solution(dirs)
