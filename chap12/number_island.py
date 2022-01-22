# leetcode 12-32 섬의 갯수
# '1'(땅)과 '0'(물)의 지도를 나타내는 m x n 2D 이진 그리드 그리드가 주어지면 섬의 수를 반환합니다.
# 섬은 물로 둘러싸여 있으며 인접한 육지를 수평 또는 수직으로 연결하여 형성됩니다. 그리드의 네 모서리가 모두 물로 둘러싸여 있다고 가정할 수 있습니다.

grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "1", "1", "0"],
    ["1", "1", "1", "0", "1"],
    ["1", "1", "1", "0", "1"]
]

## 조건1) 0,0으로부터 인접노드를 dfs한다. 더이상 찾을수 없을경우 cnt++ 한다. 검사한 노드는 전부 0으로 돌린다.
## 조건2) m,n 탐색이 종료되면 cnt를 return한다.
def num_island(grid):
    cnt = 0
    dx = [0, 0, 1, -1]  # 상하좌우 좌우이동
    dy = [1, -1, 0, 0]  # 상하이동
    m = len(grid)
    n = len(grid[0])

    # 재귀적으로 짠다 ==> 가장 중요한 idea는 1) 반복적으로 발생하는 일을 아는 것. 2) 종료 조건을 아는것.

    def dfs_recur(row, col):
        #이동할수 없거나 값이 0인경우
        if row < 0 or row >= m or col < 0 or col >= n or grid[row][col] != '1':
            return
        grid[row][col] = 0
        for i in range(4):
            dfs_recur(row + dx[i], col + dy[i])
        return

    for row in range(m):
        for col in range(n):
            node = grid[row][col]
            if node =='1':
                cnt += 1
                dfs_recur(row, col)

    return cnt

if __name__ == "__main__":
    num_island(grid)