# https://school.programmers.co.kr/learn/courses/30/lessons/42861?language=python3

# 크루스칼 알고리즘 (MST 최소 신장 트리)
# 사이클이 생기지 않도록 간선의 비중치를 고려하여 생성하는 형태

def find(parent, node):
    if parent[node] != node:
        parent[node] = find(parent, parent[node])
    return parent[node]

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def solution(n, costs):
    # 크루스칼 알고리즘 (MST 최소 신장 트리)
    # 사이클이 생기지 않도록 간선의 비중치를 고려하여 생성하는 형태
    # 비용으로 간선 정렬
    costs.sort(key=lambda x: x[2])
    parent = [i for i in range(n)]
    rank = [0] * n
    total_cost = 0

    for cost in costs:
        start, end, c = cost
        if find(parent, start) != find(parent, end):
            union(parent, rank, start, end)
            total_cost += c
    return total_cost








from collections import defaultdict
import sys

sys.setrecursionlimit(1000000)
def dfs(key,answer,node_graph,keys,visited,temp_cost):
    if len(key) > 1 and key in visited:
        return
    if set(visited) == keys:
        return min(answer,temp_cost)
    for k in node_graph[key].keys():
        temp_cost += node_graph[key][k]
        visited.append(k)
        dfs(k,answer,node_graph,keys,visited,temp_cost)
        visited.remove(k)
        temp_cost=0
    return min(answer,temp_cost)

def solution(n, costs):
    # 1. 다리를 통해 모든 섬이 이어지게만 하면 된다. > 깊이 탐색으로 들어가서 모든 노드가 원소가 될 때까지
    # 이중 딕셔너리 형태로 >> node = {0 : {1 : 3,2 : 4},...,}
    # 2. 섬을 이으면서 cost를 기록한다.
    # 종료조건 = 방문한 노드의 set이 기존 모든 노드를 가지고 있을경우. 하면서 min값을 계속해서 저장시킨다.
    # dfs에서 할일 : temp_cost를 늘리면서 현재 key에서 다음 key로 넘어간다.
    node_graph = defaultdict(dict)
    for cost in costs:
        node_graph[cost[0]][cost[1]] = cost[2]
        node_graph[cost[1]][cost[0]] = cost[2]
    keys = set(node_graph.keys())
    answer=99999999
    for key in keys:
        visited=[key]
        answer=min(answer,dfs(key,answer,node_graph,keys,visited,0))
    print(answer)
    return answer

n=4
costs=[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

print(solution(n,costs))