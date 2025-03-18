import sys

'''
오른,아래로만 이동 가능 
1,1에서 시작 n,n에서 마무리
길중 가장 큰수에 x2를 할 수 있음
현재 값이 현재까지의 가장 큰 값보다 크다면 현재까지의 값을 빼고 현재값x2를 더하고 업데이트?
오른쪽으로 전부 가고 아래로 전부 가고 만든 상태에서 dp로 
현재 값이 이전값의 max보다 크다면, 이전값의 max를 빼고, 현재값x2를 해서 더해준다.
그렇지 않다면 
'''
n = int(input())
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))
dp_no = [[0 for _ in range(n)] for _ in range(n)]
dp_yes = [[0 for _ in range(n)] for _ in range(n)]
dp_no[0][0],dp_yes[0][0] = graph[0][0],graph[0][0]*2

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue
        up_val = dp_no[i-1][j] if i>0 else -1
        left_val = dp_no[i][j-1] if j>0 else -1
        dp_no[i][j] = max(up_val,left_val) + graph[i][j]
        # 스프린쿨러 안쓸때와 쓸때를 나누어저장
        # max값은 안쓰고있다가 지금쓸때, 혹은 쓰고있는곳에서 지금값 추가만했을때 더 큰수
        up_max = max(dp_no[i-1][j]+graph[i][j]*2,dp_yes[i-1][j]+graph[i][j]) if i>0 else -1
        left_max = max(dp_no[i][j-1]+graph[i][j]*2,dp_yes[i][j-1]+graph[i][j]) if j>0 else -1
        dp_yes[i][j] = max(up_max,left_max)
        
print(dp_yes[-1][-1])
        