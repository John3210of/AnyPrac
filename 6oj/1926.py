# https://www.acmicpc.net/problem/1926
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
## bfs dp 방식
def bfs(row, col, visited, graph):
    stack = [(row, col)]
    area = 0

    while stack:
        r, c = stack.pop()
        if visited[r][c] == 1:
            continue
        visited[r][c] = 1
        area += 1

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]
        for i in range(4):
            next_row = r + dr[i]
            next_col = c + dc[i]
            if 0 <= next_row < len(graph) and 0 <= next_col < len(graph[0]) and visited[next_row][next_col] == 0 and graph[next_row][next_col] == 1:
                stack.append((next_row, next_col))

    return area

if __name__ == "__main__":
    row, col = map(int, input().split())
    graph = []
    visited = []
    count = 0
    max_area = 0
    for _ in range(row):
        line = list(map(int, input().split()))
        graph.append(line)
        visited.append([0] * col)

    for r in range(row):
        for c in range(col):
            if visited[r][c] == 0 and graph[r][c] == 1:
                area = bfs(r, c, visited, graph)
                max_area = max(max_area, area)
                count += 1
    print(count)
    print(max_area)





## dfs
import sys
sys.setrecursionlimit(3000000)
input = sys.stdin.readline

def dfs(row,col,visited,graph,area):
    # 종료조건 > visited 일때?
    if visited[row][col]==1:
        return 0
    # do something
    visited[row][col]=1
    area+=1
    # dfs seacrch
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    for i in range(4):
        next_row=row+dr[i]
        next_col=col+dc[i]
        if 0<=next_row<len(graph) and 0<=next_col<len(graph[0]) and visited[next_row][next_col]==0 and graph[next_row][next_col]==1:
            area = dfs(next_row,next_col,visited,graph,area)
    return area
if __name__ == "__main__":
    # dfs 로 size, area 구하기
    row, col = map(int, input().split())
    graph=[]
    visited=[]
    area=0
    count=0
    prev=0
    for _ in range(row):
        line=list(map(int,(input().split())))
        graph.append(line)
        visited.append([0 for _ in range(col)])

    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if visited[row][col]==0 and graph[row][col]==1:
                area = dfs(row,col,visited,graph,0)
                area = max(prev,area)
                prev=area
                count+=1
    print(count)
    print(area)

    