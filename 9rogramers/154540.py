import sys
sys.setrecursionlimit(100000)
def dfs(size,graph,visited,row,col):
    # 종료조건 : 지금 가려는 곳이 0이면종료
    # 상하좌우로 이동가능
    # visited가 1일때만 갈수있는곳, 0은 아예갈수없고 2면 이미 갔다온곳
    if row < 0 or row >= len(graph) or col < 0 or col >=len(graph[0]) or visited[row][col] != 1: ## 이 부분 때문에 범위에러가 자꾸 걸렸었음
        return size,visited
    drow=[-1,1,0,0]
    dcol=[0,0,-1,1]
    size += graph[row][col]
    visited[row][col] = 2
    for i in range(4):
        next_row = row+drow[i]
        next_col = col+dcol[i]
        size,visited = dfs(size,graph,visited,next_row,next_col)
    print(size)
    return size,visited

def solution(maps):
    answer = []
    # visited, dfs로 방문
    graph = []
    visited = []
    temp_sum = 0
    for m in maps:
        temp = []
        temp_visited = []
        for char in m:
            value = int(char) if char != 'X' else 0
            temp.append(value)
            temp_visited.append(1 if value != 0 else 0)
            temp_sum += value
        graph.append(temp)
        visited.append(temp_visited)
    if temp_sum==0:
        return [-1]
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] != 0 and visited[i][j] == 1:
                size,visited = dfs(0,graph,visited,i,j)
                answer.append(size)
    answer.sort()
    return answer
