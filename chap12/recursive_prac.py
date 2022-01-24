# graph = {
#     1: [2, 3, 4],
#     2: [5],
#     3: [5],
#     4: [],
#     5: [6, 7],
#     6: [],
#     7: [3],
# }
#
#
# def dfs_recursive(node, visited):
#     # 방문처리
#     print('append 전',visited)
#     visited.append(node)
#     print('append 후', visited)
#
#     # 인접 노드 방문
#     for adj in graph[node]:
#         print('node', node)
#         print('graph노드: ',graph[node])
#         print('adj: ',adj)
#
#         if adj not in visited:
#             print('==========================')
#             print('recursive adj,visited: ',adj,visited)
#             print('==========================')
#             dfs_recursive(adj, visited)
#
#     print('result',visited)
#     print('*==========================*')
#     return visited
#
# if __name__ == "__main__":
#     dfs_recursive(1,[])
def island_dfs_recursive(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    m = len(grid)
    n = len(grid[0])
    cnt = 0

    def dfs_recursive(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
            return

        # 방문처리
        grid[r][c] = '0'
        for i in range(4):
            dfs_recursive(r + dx[i], c + dy[i])
        return

    for r in range(m):
        for c in range(n):
            node = grid[r][c]
            if node != '1':
                continue

            cnt += 1
            dfs_recursive(r, c)
    print(cnt)
    return cnt



grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
island_dfs_recursive(grid)