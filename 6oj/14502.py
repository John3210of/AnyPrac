# https://www.acmicpc.net/problem/14502

import sys
import copy
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline

drow=[1,-1,0,0]
dcol=[0,0,1,-1]

def bfs(graph):
    temp_graph=copy.deepcopy(graph)
    queue=deque()
    for row in range(len(temp_graph)):
        for col in range(len(temp_graph[0])):
            if temp_graph[row][col] == 2:
                queue.append([row,col])
    while queue:
        row, col = queue.popleft()
        for i in range(4):
            next_row=row+drow[i]
            next_col=col+dcol[i]
            if 0<= next_row < len(temp_graph) and 0<= next_col < len(temp_graph[0]) and temp_graph[next_row][next_col]==0:
                temp_graph[next_row][next_col]=2
                queue.append([next_row,next_col])
    count=0
    for i in range(len(temp_graph)):
        count += temp_graph[i].count(0)
    return count

def backtracking(graph,count,max_count):
    if count==3:
        count = bfs(graph)
        return max(count,max_count)
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col]==0:
                graph[row][col]=1
                max_count = backtracking(graph,count+1,max_count)
                graph[row][col]=0
    return max_count

if __name__ == "__main__":
    n,m = map(int,input().split())
    graph=[]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    max_count = backtracking(graph,0,0)
    print(max_count)
    