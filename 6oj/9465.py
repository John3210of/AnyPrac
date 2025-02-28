import sys
input = sys.stdin.readline

def solution(graph):
    # 최대 뜯을수 있는 스티커의 수는 k개를 넘을수없다.
    # 가장 큰 수를 매번 구해내는것도 별로고
    # 뜯는 조건은 근처의 합보다 내가 크거나 같다면?
    dp=[0 for _ in range(10)]
    count=0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j]>0:
                point = tear_sticker(i,j,graph)
                if point > 0:
                    count+=1
                    dp[count]=dp[count-1]+point
    return dp[count]

def tear_sticker(row,col,graph):
    drow=[-1,1,0,0]
    dcol=[0,0,-1,1]
    arround_sum=0
    arround_axis=[]
    for i in range(4):
        next_row=row+drow[i]
        next_col=col+dcol[i]
        if 0<=next_row<len(graph) and 0<=next_col<len(graph[0]):
            arround_sum+=graph[next_row][next_col]
            arround_axis.append([next_row,next_col])
    if arround_sum < graph[row][col]:
        point=graph[row][col]
        graph[row][col]=0
        for arround_r,arround_c in arround_axis:
            graph[arround_r][arround_c]=0
    else:
        point=0
    return point

if __name__ == "__main__":
    n = int(input())
    answer=[]
    for i in range(n):
        k=int(input())
        graph=[]
        for _ in range(2):
            graph.append(list(map(int,input().split())))
        answer.append(solution(graph))
    for ans in answer:
        print(ans)