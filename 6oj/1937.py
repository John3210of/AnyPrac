import sys
sys.setrecursionlimit(3000000)
input = sys.stdin.readline
# dfs로 탐색이 끝났을때, 총 이동거리를 알면 되는 문제인데
# 각 분기별로 함수의 실행이 종료될때, max_distance를 갱신해야함
# 현재 좌표에서 최대거리를 구하고, dp에 저장
# 현재 좌표에서 다음 좌표로 넘어갈때, dp에 값이 이미 저장되어있다면 1+next_length로 대체가 가능함
def dfs(graph,row,col,dp):
    if dp[row][col]!=-1:
        return dp[row][col]
    drow=[1,-1,0,0]
    dcol=[0,0,1,-1]
    max_distance=1
    for i in range(4):
        next_row=row+drow[i]
        next_col=col+dcol[i]
        if 0<=next_row<len(graph) and 0<=next_col<len(graph[0]) and graph[next_row][next_col] > graph[row][col]:
            max_distance=max(max_distance,dfs(graph,next_row,next_col,dp)+1)
    dp[row][col]=max_distance
    for i in dp:
        print(i)
    print('*'*30)
    return dp[row][col]


if __name__ == "__main__":
    n = int(input())
    graph=[]
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    dp = [[-1 for _ in range(len(row))] for row in graph]
    max_distance=0
    for row in range(len(graph)):
        for col in range(len(graph[row])):
            max_distance=max(max_distance,dfs(graph,row,col,dp))
    print(max_distance)

# import sys
# sys.setrecursionlimit(300000)
# input = sys.stdin.readline

# def dfs(graph,row,col,prev,distance,dic):
#     if graph[row][col] <= prev:
#         return
#     drow=[1,-1,0,0]
#     dcol=[0,0,1,-1]
#     dic[distance]+=1
#     for i in range(4):
#         next_row=row+drow[i]
#         next_col=col+dcol[i]
#         if 0<=next_row<len(graph) and 0<=next_col<len(graph[0]):
#             dfs(graph,next_row,next_col,graph[row][col],distance+1,dic)

# from collections import defaultdict
# if __name__ == "__main__":
#     # 모든점에서 시작하여 이동거리를 각각 저장?
#     # 맨처음에 상하좌우를 확인하고 가 의미가 없을듯?
#     # 이동한 거리를 갱신하면서 가고, 더이상 이동할수 없을때에 함수가 종료되면서 거리를 return
#     # dictionary에 depth를 계속 기록하면 되지 않을까? > 시간초과
#     n = int(input())
#     graph=[]
#     for _ in range(n):
#         graph.append(list(map(int, input().split())))
#     dp = [[0 for _ in range(len(row))] for row in graph]
#     dic=defaultdict(int)
#     for row in range(len(graph)):
#         for col in range(len(graph[row])):
#             dfs(graph,row,col,-1,1,dic)
#     print(max(dic.keys()))