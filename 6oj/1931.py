import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    graph=[]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    graph.sort(key=lambda x:(x[1],x[0]))
    count=1
    end=graph[0][1]
    # 끝나는시간이 시작시간일경우
    for i in range(1,len(graph)):
        if end <= graph[i][0]:
            end=graph[i][1]
            count+=1
    print(count)