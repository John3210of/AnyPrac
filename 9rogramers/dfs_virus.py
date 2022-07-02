import sys

sys.setrecursionlimit(100000)


def solution(rows, columns, max_virus, queries):
    # result = [[0 for _ in range(columns)] for _ in range(rows)]
    result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    # 상 하 좌 우
    drow = [-1, 1, 0, 0]
    dcol = [0, 0, -1, 1]

    def dfs(row, col):
        for j in range(4):  # 찍은 좌표가 맥스와 같거나 더 큰경우
            targetRow = row + drow[j]
            targetCol = col + dcol[j]
            if targetRow < 0 or targetCol < 0 or targetRow >= rows or targetCol >= columns:  # 그래프 안에서 나가면 안됨
                continue
            else:
                if result[targetRow][targetCol] < max_virus:
                    result[targetRow][targetCol] += 1  # 찍은 좌표가 맥스보다 작을경우
                else:
                    dfs(targetRow, targetCol)
        return result

    for i in range(len(queries)):
        row = queries[i][0] - 1
        col = queries[i][1] - 1
        if result[row][col] < max_virus:
            result[row][col] += 1  # 찍은 좌표가 맥스보다 작을경우
        else:
            dfs(row, col)

    return result


rows = 3
columns = 4
max_virus = 2
queries = [[3, 2], [3, 2], [2, 2], [3, 2], [1, 4], [3, 2], [2, 3], [3, 1]]

solution(rows, columns, max_virus, queries)


