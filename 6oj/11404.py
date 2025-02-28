import sys
input = sys.stdin.readline

def solution():
    return 0

if __name__ == "__main__":
    n = int(input())
    m = int(input())
    graph=[[float('inf') if i!=j else 0 for i in range(n)] for j in range(n)]
    print(graph)
    for _ in range(m):
        row,col,cost=map(int,input().split())
        graph[row-1][col-1]=cost
    print(graph)
    