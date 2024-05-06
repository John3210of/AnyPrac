# https://www.acmicpc.net/problem/4179
import sys
from collections import deque
input = sys.stdin.readline
def bfs(graph,f_queue,j_queue,f_visited,j_visited,row,col):
    drow = [1, -1, 0, 0]
    dcol = [0, 0, 1, -1]
    while f_queue:
        temp_row, temp_col = f_queue.popleft()
        for i in range(4):
            next_row = temp_row + drow[i]
            next_col = temp_col + dcol[i]
            if 0 <= next_row < row and 0 <= next_col < col:
                if not f_visited[next_row][next_col] and graph[next_row][next_col] != '#':
                    f_visited[next_row][next_col] = f_visited[temp_row][temp_col] + 1
                    f_queue.append((next_row, next_col))
    while j_queue:
        temp_row, temp_col = j_queue.popleft()
        for i in range(4):
            next_row = temp_row + drow[i]
            next_col = temp_col + dcol[i]
            if 0 <= next_row < row and 0 <= next_col < col:
                # 간적이 없거나, 길로만
                # 거기서 불이 아예 없거나,불이 있어도 진행도보다 큰 값이 되었을때 붙는다면 관계없음
                if not j_visited[next_row][next_col] and graph[next_row][next_col] == '.':
                    if f_visited[next_row][next_col] ==0 or f_visited[next_row][next_col] > j_visited[temp_row][temp_col] + 1:
                        j_visited[next_row][next_col] = j_visited[temp_row][temp_col] + 1
                        j_queue.append((next_row, next_col))
            else: # out of range
                return j_visited[temp_row][temp_col] + 1
    return 'IMPOSSIBLE'
 
if __name__ == "__main__":
    row, col = map(int, input().split())
    graph = [list(input().strip()) for _ in range(row)]
    f_queue, j_queue = deque(), deque()
    f_visited, j_visited = [[0] * col for _ in range(row)], [[0] * col for _ in range(row)]
    # 퍼지는 것을 나누어 계산 시키며 fire queue에 해당하는 숫자보다 작을때만 통과 시킴. 
    # list out of range 일 때, visited+1을 return
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 'F':
                f_queue.append((i, j))
            elif graph[i][j] == 'J':
                j_queue.append((i, j))
    print(bfs(graph,f_queue,j_queue,f_visited,j_visited,row,col))

'''
반례: 
5 5
FFFFF
..J..
.....
.....
.....
'''
