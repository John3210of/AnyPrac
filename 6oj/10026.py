# https://www.acmicpc.net/problem/10026
import sys
sys.setrecursionlimit(100000)

# dfs로 같은 경우의 size,visited를 모두 측정함
# 일반과 색약의 그래프를 따로 저장해서 size를 둘다 반환하도록 함
# 방문 했던 곳을 제외하고 dfs로 탐색시킴

def dfs(graph,visited,size,row,col):
    # 종료조건 > visited=1
    if visited[row][col]==1:
        return
    visited[row][col]=1
    dr=[1,-1,0,0]
    dc=[0,0,1,-1]
    for i in range(4):
        next_row = row+dr[i]
        next_col = col+dc[i]
        if 0<=next_row<len(graph) and 0<=next_col<len(graph[0]) and graph[row][col]==graph[next_row][next_col]:
            dfs(graph,visited,size,next_row,next_col)

def solution(graph):
    visited = [[0 for _ in range(len(row))] for row in graph]
    size=0
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if visited[row][col]==0:
                dfs(graph,visited,size,row,col)
                size+=1
    return size

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    graph=[]
    rg_graph=[]
    for _ in range(n):
        line=input().strip()
        graph.append(list(line))
        rg_graph.append(list(line.replace('R','G')))
    print(solution(graph),solution(rg_graph))

    # graph=[['R', 'R', 'G', 'G', 'G'], ['B', 'B', 'B', 'B', 'B'], ['R', 'R', 'R', 'R', 'R']]
    # rg_graph=[['G', 'G', 'G', 'G', 'G'], ['B', 'B', 'B', 'B', 'B'], ['G', 'G', 'G', 'G', 'G']]
    # print(solution(graph),solution(rg_graph))
    
