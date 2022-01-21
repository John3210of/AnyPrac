graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


def dfs_recursive(node, visited):
    # 방문처리
    print('append 전',visited)
    visited.append(node)
    print('append 후', visited)

    # 인접 노드 방문
    for adj in graph[node]:
        print('node', node)
        print('graph노드: ',graph[node])
        print('adj: ',adj)

        if adj not in visited:
            print('==========================')
            print('recursive adj,visited: ',adj,visited)
            print('==========================')
            dfs_recursive(adj, visited)

    print('result',visited)
    print('*==========================*')
    return visited

if __name__ == "__main__":
    dfs_recursive(1,[])
