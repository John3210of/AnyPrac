import sys
from collections import deque

def find_ghost_distance(start,end):
    distance = abs(start[0]-end[0]) + abs(start[1]-end[1])
    return distance
    
def find_human_distance(start, end, graph):
    '''
    BFS
    '''
    queue = deque([(start[0], start[1], 0)])
    visited = set()
    visited.add((start[0], start[1]))
    
    drow = [1, -1, 0, 0]
    dcol = [0, 0, 1, -1]
    
    while queue:
        row, col, dist = queue.popleft()
        if [row, col] == end:
            return dist
        
        for i in range(4):
            next_row = row + drow[i]
            next_col = col + dcol[i]
            if (0 <= next_row < len(graph) and 0 <= next_col < len(graph[0]) 
                    and graph[next_row][next_col] != '#' and (next_row, next_col) not in visited):
                visited.add((next_row, next_col))
                queue.append((next_row, next_col, dist + 1))
    return float('inf')

row, col = map(int,input().split())
graph = []
ghosts = []
for i in range(row):
    string = str(input())
    rows = []
    for j in range(len(string)):
        if string[j] == 'N':
            namwoo = [i,j]
        elif string[j] == 'G':
            ghosts.append([i,j])
        elif string[j] == 'D':
            escape = [i,j]
        rows.append(string[j]) 
    graph.append(rows)
namwoo_to_escape = find_human_distance(namwoo,escape,graph)
answer = 'Yes'
for ghost in ghosts:
    distance_to_escape = find_ghost_distance(ghost,escape)
    if distance_to_escape <= namwoo_to_escape:
        answer = 'No'
if namwoo_to_escape == float('inf'):
    answer = 'No'

print(answer)
