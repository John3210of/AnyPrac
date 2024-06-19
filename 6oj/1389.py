import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n,m = map(int, input().split())
    graph=[[float('inf') if i!=j else 0 for i in range(n)] for j in range(n)]
    for _ in range(m):
        a,b = map(int, input().split())
        graph[a-1][b-1]=1
        graph[b-1][a-1]=1
    # 최단거리 구하기
    # 각 노드에서 모든 다른 노드를 방문할때의 비용이 최소가 되는 값을 리턴
    # 본인-본인 가중치는 0으로 두고, 바로 이어지는 경우는 1로 둔다.
    # 이어질수 없는 경우는 탐색하는데 a,n -> n,b 의 비용과 비교하여 a,b의 비용을 갱신한다.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    answer_idx=-1
    answer_sum=float('inf')
    for i,lst in enumerate(graph):
        if sum(lst) < answer_sum:
            answer_sum=sum(lst)
            answer_idx=i
    print(answer_idx+1)