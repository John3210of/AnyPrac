# https://www.acmicpc.net/problem/1012
import sys
sys.setrecursionlimit(100000)

def dfs(graph, row, col, visited):
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]
    # 방문하지 않은 배추인 경우에만 탐색
    if visited[row][col] == 0 and graph[row][col] == 1:
        visited[row][col] = 1
        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]
            if 0 <= next_row < len(graph) and 0 <= next_col < len(graph[0]):
                dfs(graph, next_row, next_col, visited)

def solution(graph):
    # 그래프 전체를 탐색하면서 배추 덩어리 찾기
    # 배추가 있고 방문하지 않은 경우에만 DFS 탐색 수행
    count = 0
    visited = [[0] * len(graph[0]) for _ in range(len(graph))]
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col] == 1 and visited[row][col] == 0:
                dfs(graph, row, col, visited)
                count += 1
    return count

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    answer = []
    # 테스트 케이스별로 그래프 입력받고 해결
    for _ in range(n):
        m, n, k = map(int, input().split())
        graph = [[0] * m for _ in range(n)]
        for _ in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1
        answer.append(solution(graph))
    for result in answer:
        print(result)