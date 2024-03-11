# https://school.programmers.co.kr/learn/courses/30/lessons/1844?language=python3 게임맵최단거리
import copy

maps=[[2,0,1,1,1],
      [1,0,1,0,1],
      [1,0,1,1,1],
      [1,1,1,0,1],
      [0,0,0,0,1]]

# 종료조건은 [4,4]에 도착했을때 종료
# 1이면 건너가고 이동거리증가를 상하좌우에 넣는다.
# 도착시에 이동거리를 answer list에 넣는다 x가 열의개수 y가 행의개수
drow=[-1,1,0,0]
dcol=[0,0,-1,1]
def dfs(maps,visited,answer_list,moving_times,cursor):
      print(cursor)
      if cursor==[4,4]:
            answer_list.append(moving_times)
            return answer_list

      for i in range(4):
            next_row = cursor[0]+drow[i]
            next_col = cursor[1]+dcol[i]
            if 0<=next_row<len(maps) and 0<=next_col<len(maps[0]) and visited[next_row][next_col]==1:
                  visited[next_row][next_col]=2
                  moving_times+=1
                  dfs(maps,visited,answer_list,moving_times,[next_row,next_col])
      return answer_list

def solution(maps):
      visited=copy.deepcopy(maps)
      answer_list=dfs(maps,visited,[],0,[0,0])
      print(answer_list)
      return min(answer_list)

# 최단거리문제는 dfs로 풀면 안됨

from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[False] * m for _ in range(n)]
    drow = [-1, 1, 0, 0]
    dcol = [0, 0, -1, 1]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True

    while queue:
        row, col, distance = queue.popleft()
        if row == n - 1 and col == m - 1:
            return distance
        for i in range(4):
            next_row = row + drow[i]
            next_col = col + dcol[i]
            if 0 <= next_row < n and 0 <= next_col < m and maps[next_row][next_col] == 1 and not visited[next_row][next_col]:
                visited[next_row][next_col] = True
                queue.append((next_row, next_col, distance + 1))
    return -1

maps = [
    [1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 1]
]

print(solution(maps)) 

