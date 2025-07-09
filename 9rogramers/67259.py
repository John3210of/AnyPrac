from collections import deque

def solution(board):
    '''
    최단거리 방향에따라 비용추가
    완탐?
    dp?
    최소 비용
    3차원 dp + bfs
    '''
    N = len(board)
    points = [[[float('inf')] * 4 for _ in range(N)] for _ in range(N)]
    queue = deque()
    drow = [1, -1, 0, 0]
    dcol = [0, 0, 1, -1]
    answer = []
    
    if board[0][1] == 0:
        points[0][1][2] = 100
        queue.append([0, 1, 2, 100])
    if board[1][0] == 0:
        points[1][0][0] = 100
        queue.append([1, 0, 0, 100])
    
    while queue:
        row, col, direction, cost = queue.popleft()
        if row == N-1 and col == N-1:
            answer.append(cost)
        for i in range(4):
            next_row = row + drow[i]
            next_col = col + dcol[i]
            next_direction = i
            if 0 <= next_row < N and 0 <= next_col < N and board[next_row][next_col] == 0:
                if next_direction == direction:
                    next_cost = cost + 100
                else:
                    next_cost = cost + 600
                if next_cost < points[next_row][next_col][next_direction]:
                    points[next_row][next_col][next_direction] = next_cost
                    queue.append([next_row, next_col, next_direction, next_cost])
    
    return min(points[N-1][N-1])



from collections import deque
def solution(board):
    '''
    최단거리 방향에따라 비용추가
    완탐?
    dp?
    최소 비용
    '''
    visited = [[0 for _ in range(len(board))] for _ in range(len(board))]
    visited[0][0] = 1
    queue = deque([[1,0,'down',100],[0,1,'right',100]])
    directions = ['down','up','right','left']
    drow = [1,-1,0,0]
    dcol = [0,0,1,-1]
    points = [[float('inf') for _ in range(len(board))] for _ in range(len(board))]
    points[0][0] = 0
    points[1][0] = 100
    points[0][1] = 100
    visited[0][1]=1
    visited[1][0]=1
    answer = []
    while queue:
        row, col, direction, cost = queue.popleft()
        if cost == 1200:
            print(row,col,direction)
        if [row+1, col+1] == [len(board), len(board)]:
            answer.append(cost)
        for i in range(4):
            next_row = row + drow[i]
            next_col = col + dcol[i]
            next_direction = directions[i]
            if 0 <= next_row < len(board) and 0 <= next_col < len(board) and board[next_row][next_col] == 0:
                if direction == next_direction:
                    next_point = min(points[row][col] + 100, points[next_row][next_col])
                else:
                    next_point = min(points[row][col] + 600, points[next_row][next_col])
                if next_point <= points[next_row][next_col]:
                    queue.append([next_row,next_col,next_direction,next_point])
                    points[next_row][next_col] = next_point
        print(points)
    '''
    [0,   100, 200,  300,  400,  500,  600,  inf], 
    [100, 700, 800,  900,  1000, 1100, 1200, 1300], 
    [200, 800, 900,  1000, 1100, inf,  1800, 1900], 
    [300, 900, 1000, 1100, inf,  2500, 1900, 2000], 
    [400, 1000,1100, inf,  2700, 2600, 2000, inf], 
    [500, 1100, inf, 3400, 3300, 3200, inf,  5000],
    [600, inf, 4100, 4000, 3400, inf,  4800, 4900], 
    [inf, 4300,4200, 4100, 3500, 4100, 4200, 4300]]
    '''
    return min(answer)

solution(	[[0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 0, 1, 0], [0, 1, 0, 0, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0, 0]])