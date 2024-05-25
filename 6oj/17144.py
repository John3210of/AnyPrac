# https://www.acmicpc.net/problem/17144

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def get_air_fresh(graph):
    air_fresh=[]
    for row in range(len(graph)):
        if -1 in row:
            air_fresh.append(row,row+1)
    return air_fresh

def spread_dust(graph):
    temp_spread_graph = [[0 for _ in range(len(row))] for row in graph]
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            spread_amount=graph[row][col]//5
            if spread_amount>0:
                update_graph_and_temp_graph(spread_amount,row,col,graph,temp_spread_graph,air_fresh)
    
    for row in range(len(graph)):
        for col in range(len(graph[0])):
            if graph[row][col]>=0:
                graph[row][col]+=temp_spread_graph[row][col]

def update_graph_and_temp_graph(spread_amount,row,col,graph,temp_spread_graph,air_fresh):
    drow=[-1,1,0,0]
    dcol=[0,0,-1,1]
    for i in range(4):
        next_row=row+drow[i]
        next_col=col+dcol[i]
        if 0<=row<len(graph) and 0<=col<len(graph[0]) and next_row not in air_fresh:
            temp_spread_graph[next_row][next_col]+=spread_amount
            graph[row][col]-=spread_amount

def operate_air_fresh(graph,air_fresh):
    top=air_fresh[0]
    bottom=air_fresh[1]
    turn_counter_clockwise(graph,top)
    turn_clockwise(graph,bottom)

def turn_counter_clockwise(graph,top):
    right_val = push_row_right(graph,top)
    up_val = push_col_up(graph,len(graph[0])-1,right_val)
    left_val = push_row_left(graph,0,up_val)
    push_col_down(graph,0,left_val)
    graph[top][0] = -1

def turn_clockwise(graph,bottom):
    is_top=False
    right_val = push_row_right(graph,bottom)
    down_val = push_col_down(graph,len(graph[0])-1,right_val,is_top)
    left_val = push_row_left(graph,len(graph)-1,down_val)
    push_col_up(graph,0,left_val,is_top)
    graph[bottom][0] = -1

def push_row_right(graph,row):
    pass

def push_row_left(graph,row,insert_val):
    pass

def push_col_down(graph,col,insert_val,is_top=True):
    pass

def push_col_up(graph,col,insert_val,is_top=True):
    pass

if __name__ == "__main__":
    '''
    1. 공기청정기 위치 찾기(1열로 한정)
    2. 먼지확산 임시 그래프 만들기
    3. 임시확산 그래프에 확산될 양 누적시키기 + 기존 그래프에 확산시킬양 빼주기
    4. 임시확산 그래프 + 기존그래프
    5. 공기 밀기 (시계, 반시계 구현)
    6. 2~5를 T회 반복
    7. 그래프의 미세먼지값 합계를 출력
    '''
    r, c, t = map(int, input().split())
    graph=[]
    for i in range(r):
        graph.append(list(map(int,input().split())))
    air_fresh=get_air_fresh(graph)
    print(graph)
    for _ in range(t):
        spread_dust(graph)
        operate_air_fresh(graph,air_fresh)
    total_dust = -2
    for row in graph:
        total_dust+=sum(row)
    print(total_dust)