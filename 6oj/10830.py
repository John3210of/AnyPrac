import sys
input = sys.stdin.readline

def multiple_matrix(A,B):
    answer=[[0 for _ in range(len(A))] for _ in range(len(B[0]))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            # graph 의 i행과 j 열을 1:1로 곱하여 더한값 answer[i][j]
            for k in range(len(A)):
                answer[i][j]+=A[i][k]*B[k][j]
            answer[i][j]%=1000
    return answer

if __name__ == "__main__":
    n,b = map(int, input().split())
    graph=[]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    if b==1:
        answer=graph
    else:
        answer=multiple_matrix(graph,graph)
        if b>2:
            for _ in range(b-2):
                answer=multiple_matrix(answer,graph)
    for row in answer:
        print(' '.join(map(str,row)))