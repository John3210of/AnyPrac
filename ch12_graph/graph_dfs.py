# 연결되는 정점과 정점간의 관계를 표현한다.

# 선형구조 = 자료를 저장, 꺼내는 것에 초점을 둠
# 비선형 = 표현에 초점을 둠

# 간선 = edge // 정점(vertex) = node // 인선노드 = 간접으로 연결된 노드.

# 그래프는 유 방향과 무 방향으로 나뉜다.
# follow //  friend

# 표현방법 :  1) 인접 행렬 => 탐색비용이 항상 1이다  2) 인접 리스트 => 공간 복잡도가 작으니 메모리 아낄수있다

# dfs : 깊이 우선 탐색  <=>  bsf : 넓이 우선 탐색

# 재귀적으로 짠다 ==> 가장 중요한 idea는 1) 반복적으로 발생하는 일을 아는 것. 2) 종료 조건을 아는것.
# 인접노드 = adj ad jsont

# 섬의 갯수 leetcode 200.

# Q200) '1'(땅)과 '0'(물)의 지도를 나타내는 m x n 2D 이진 그리드 그리드가 주어지면 섬의 수를 반환합니다.
#       섬은 물로 둘러싸여 있으며 인접한 육지를 수평 또는 수직으로 연결하여 형성됩니다.
#       그리드의 네 모서리가 모두 물로 둘러싸여 있다고 가정할 수 있습니다.
# 제약:
#   m == grid.length
#   n == 그리드[i].길이
#   1 <= m, n <= 300
#   grid[i][j]는 '0' 또는 '1'입니다.

# 궁금한게 뭐였는가? stack방식으로 풀었을때와 recursive하게 풀었을때. 어떤 차이가 발생하는지?

# 해야할 것.
# 해보니까 ~~더라.
# ~~만큼의 시간이 걸리더라.

import math
import time

def island_dfs_stack(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            cnt += 1
            stack = [(row, col)]

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    stack.append((nx, ny))
    return cnt


assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_stack(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3


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

    return cnt


assert island_dfs_recursive(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_recursive(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3



if __name__ == "__main__":

    Map=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]


    start = time.time()
    island_dfs_stack(Map)
    math.factorial(100000)
    end = time.time()
    print(f"{end - start:.5f} sec")

    start = time.time()
    island_dfs_recursive(Map)
    math.factorial(100000)
    end = time.time()
    print(f"{end - start:.5f} sec")