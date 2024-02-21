import sys

# 아오 재귀제한시치
sys.setrecursionlimit(1000000)
# https://school.programmers.co.kr/learn/courses/30/lessons/250136?language=python3 석유시추하기
# 0,0 부터 dfs. 탐색범위 내에 1일경우 visted = True, 너비 갱신하여 dfs
# visited 로 탐색된 위치거나 0일경우 너비 0으로 리턴
# cnt, size를 원소로 갖는 리스트를 반환하여 visited 의 값을 바꾼다

def dfs(land, visited, row, col, cnt):
    if row < 0 or row >= len(land) or col < 0 or col >= len(land[0]) or land[row][col] == 0 or visited[row][col]:
        return 0
    visited[row][col] = cnt
    size = 1
    size += dfs(land, visited, row + 1, col,cnt)
    size += dfs(land, visited, row - 1, col,cnt)
    size += dfs(land, visited, row, col + 1,cnt)
    size += dfs(land, visited, row, col - 1,cnt)
    
    return size

def count_connected_components(land):
    rows, cols = len(land), len(land[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    cnt = -1
    target_list = []

    for i in range(rows):
        for j in range(cols):
            if land[i][j] == 1 and not visited[i][j]:
                component_size = dfs(land, visited, i, j, cnt)
                target_list.append([cnt,component_size])
                cnt-=1
    return target_list, visited

land = [[1, 0, 1, 0, 1, 1], 
        [1, 0, 1, 0, 0, 0], 
        [1, 0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 0, 0], 
        [1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0], 
        [1, 1, 1, 1, 1, 1]]

target_list, visited = count_connected_components(land)
transposed_visited = [list(row) for row in zip(*visited)]
partial_set_list = []
for i in transposed_visited:
    partial_set_list.append(set(i))
target_dict = dict(target_list)
temp_list=[]
for i in range(len(partial_set_list)):
    temp=0
    for j in partial_set_list[i]:
        if j != 0:
            temp+=target_dict[j]
    temp_list.append(temp)
print(max(temp_list))