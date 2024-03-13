# https://school.programmers.co.kr/learn/courses/30/lessons/92343 양과늑대 이해하는데 매우 오래걸림.
def dfs(sheep, wolf, cur_node, next_nodes, info, graph):
    if info[cur_node] == 0:
        sheep += 1
    else:
        wolf += 1
        
    answer = sheep
    if sheep <= wolf:
        return answer
        
    for idx, next_node in enumerate(next_nodes):
        next_candidates = next_nodes[:idx] + next_nodes[idx+1:]  # next_nodes의 복사로 next_candidates를 만들되, 현재 인덱스의 값을 제외한 나머지 값을 사용
        next_candidates.extend(graph[next_node])
        answer = max(answer, dfs(sheep, wolf, next_node, next_candidates, info, graph))

    return answer

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    print(graph)
    # 그래프를 초기화, 선언
    # 0번노드에서 시작한다.
    # dfs 종료조건 => sheep = wolf
    # 현재 존재하는 노드에서, 후보군에 해당하는 점들을 방문할것. 방문객 명단은 기존 후보군+ n+1차례에서 갈 후보군
    for edge in edges:
        graph[edge[0]].append(edge[1])
    next_nodes = graph[0]
    a = dfs(0, 0, 0, next_nodes, info, graph)
    print(graph)
    return a

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
print(solution(info, edges))  # Output: 5