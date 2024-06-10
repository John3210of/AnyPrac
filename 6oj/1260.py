import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(graph,v,visited,answer):
    visited[v]=True
    answer.append(v)
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited,answer)
    return answer

def bfs(graph,v,visited_2,answer):
    queue=deque([v])
    visited_2[v]=True
    while queue:
        node = queue.popleft()
        answer.append(node)
        for neighbor in graph[node]:
            if not visited_2[neighbor]:
                queue.append(neighbor)
                visited_2[neighbor]=True
    return answer

if __name__ == "__main__":
    n, m, v = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for key in graph:
        key.sort()
    visited=[False for _ in range(n+1)]
    visited_2=[False for _ in range(n+1)]
    dfs_result = dfs(graph, v, visited, [])
    bfs_result = bfs(graph, v, visited_2, [])
    print(" ".join(map(str, dfs_result)))
    print(" ".join(map(str, bfs_result)))
    # 아 ... 개화나네 아................ ...........
    '''
import sys
from collections import defaultdict,deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(dic,v,visited,answer):
    visited[v]=True
    answer.append(v)
    print(answer)
    for i in dic[v]:
        if not visited[i]:
            dfs(dic,i,visited,answer)
    return answer

def bfs(dic,v,visited,answer):
    queue=deque([v])
    visited[v]=True
    while queue:
        node = queue.popleft()
        answer.append(node)
        print(answer)
        for neighbor in dic[node]:
            if not visited[neighbor] and node not in queue:
                queue.append(neighbor)
                visited[neighbor]=True
    return answer

if __name__ == "__main__":
    dic=defaultdict(list)
    n, m, v = map(int, input().split())
    for _ in range(m):
        a,b = map(int, input().split())
        if b not in dic[a] and a not in dic[b]:
            dic[a].append(b)
            dic[b].append(a)
    for key in dic:
        dic[key].sort()
    print(dic)
    visited=[False for _ in range(n+1)]
    visited_2=[False for _ in range(n+1)]
    print(dfs(dic,v,visited,[]))
    print(bfs(dic,v,visited_2,[]))
    
    '''