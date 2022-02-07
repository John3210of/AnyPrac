import heapq

INF = int(1e9)
n, m = map(int, input().split())  # n = 노드갯수 // m= 간선갯수
graph = [[] for i in range(n + 1)]
# 간선과의 정보 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append([b, 1])
    graph[b].append([a, 1])

x, k = map(int, input().split())  # x 최종노드 , k 거쳐갈노드


# x가 최종 도착지, k는 거쳐야할곳 그렇다면 (1,1)>k로 가는 최단거리와 k>x로 가는 최단거리를 더해주면 되겟슴
# 1과 인접한 노드의 길이를 갱신해주고 누적값을 더해가라. # 만약 inf라면 -1을 출력한다.
def dijk(graph, start, end):
    N = len(graph)
    dist = [INF] * N
    q = []
    heapq.heappush(q, (0, start))  # 넣을 위치,( 누적비용 , 시작위치) 팝할때 맨 좌측기준으로 팝된다. 누적비용
    dist[start] = 0
    print('dist start!: ', dist)
    while q:
        acc, pointer = heapq.heappop(q)  # 누적값, 현재노드 위치
        print('우선순위 큐 상태 : ', q)
        if dist[pointer] < acc:  # 나의 노드를 기준으로 최솟값이 갱신이 이미 되었다고 볼 수 있다.
            continue
        for adj, temp in graph[pointer]:  # adj = 인접노드, temp=현재 위치까지의 비용
            cost = acc + temp
            if cost < dist[adj]:  # cost가 시작점 기준 인접노드의 거리보다 더 작은경우
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))
                print('push후 우선순위 큐: ', q)
                print('dist 갱신 후: ', dist)

    return dist[end]


# k가 들러야되는곳 x가 종착지
r1 = dijk(graph, 1, k)
r2 = dijk(graph, k, x)
print(r1 + r2)
