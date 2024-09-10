# 그래프의 고정된 한 노드에서, 다른 모든 노드로의 최단거리를 찾는 알고리즘
# 조건으로 비음수 간선을 가진 그래프에서만 사용 가능하며, 음수 가중치가 있는 경우 벨만-포드 알고리즘을 선택해야한다.
# PRIORITY QUEUE, GREEDY, DP를 적절히 사용하여 해결한다.

#pseudo code
'''
Input : 그래프 G, 출발점 start
Output : 출발점에서 각 정점까지의 최단 거리

1. 모든 노드에 대해 최단거리 배열 dist[]를 초기화한다.
FOR each node N in G:
    dist[N] = 1e9 # 모든 정점의 거리를 무한대로 초기화
ENDFOR
dist[start] = 0 # 시작점 초기화

2. priority queue를 초기화하고, 시작점을 넣는다.
priority_queue.push((0,start)) # (거리,정점)

3. pq에서 뽑아낸 노드와 인접한 노드를 탐색하고, 인접한 노드까지의 거리를 갱신한다. 이때 기존 거리보다 거리가 작다면 갱신한다.
갱신되었다면 우선순위큐에 거리와 노드번호를 다시 삽입한다.
이 행위를 pq가 존재하는 동안 반복한다.
distance, node = heapq.heappop(pq)
WHILE priority_queue exists:
    FOR neighbor, weight in graph[node]:
        distance += weight
        IF distance < dist[neighbor]:
            dist[neighbor] = distance
            heapq.heappush(pq,(distance,neighbor))
    ENDFOR
ENDWHILE

RETURN dist
'''

# 예제 https://school.programmers.co.kr/learn/courses/30/lessons/12978?language=python3
'''
INPUT : 마을의 개수 N, 노드 가중치(음수 없음) road, 거리의 최대값 K
- input condition : road = a, b(1 ≤ a, b ≤ N, a != b),c

OUTPUT : 1번 마을에서 다른 마을까지의 거리가 k 이하인 개수를 return

- 단일노드로부터 이므로 다익스트라가 시간복잡도에서 유리하다?
근데 걍 플로이드워셜을 start=1로 고정하면? 시간복잡도 O(n^2)
다익스트라는 pq를 이용하므로 (n+e)log(n)

# pseudo code 초안
initailize start_end_distance_list 'inf' 
initailize EMPTY graph[][]
FOR start,end,cost from road:
    graph[start-1] = [end-1,cost] # for easy indexing
push start_point priority_queue as pq = [start_node=0,cost=0]
WHILE pq exists:
    total_cost, node = pq.pop()
    FOR connected_node, cost from graph(node):
        total_cost += cost
        IF dist[connected_node] > total_cost:
            dist[connected_node] = total_cost
            pq.push(total_cost,connected_node)
        ENDIF
    ENDFOR
ENDWHILE

# pseudo code mk2 ft. gpt
initialize dist[] to 'inf' for all nodes
initialize EMPTY graph[][]
FOR start, end, cost FROM road:
    graph[start-1].append((end-1, cost))  # Using list of edges for each node
ENDFOR
initialize priority_queue pq = [(0, start_node)]  # (cost, node) starting from the start_node
dist[start_node] = 0
WHILE pq exists:
    current_cost, node = pq.pop()
    # If we have already found a better way to reach this node, continue
    IF current_cost > dist[node]:
        continue
    ENDIF
    FOR connected_node, cost IN graph[node]:
        new_cost = current_cost + cost

        IF dist[connected_node] > new_cost:
            dist[connected_node] = new_cost
            pq.push((new_cost, connected_node))
        ENDIF
    ENDFOR
ENDWHILE
'''

import heapq
def solution(N, road, K):
    dist=[float('inf') for _ in range(N)]
    dist[0]=0
    graph=[[] for _ in range(N)]
    pq=[]
    for start, end, cost in road:
        graph[start-1].append([end-1,cost])
        graph[end-1].append([start-1,cost])
    heapq.heappush(pq,[0,0])
    while pq:
        current_cost, node = heapq.heappop(pq)
        if current_cost > dist[node]:
            continue
        for connected_node, cost in graph[node]:
            new_cost = current_cost + cost
            if dist[connected_node] > new_cost:
                dist[connected_node] = new_cost
                heapq.heappush(pq,[new_cost, connected_node])
    answer=0
    for v in dist:
        if v<=K:
            answer+=1
    return answer