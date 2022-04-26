def rotate(key):
    row = len(key)  # row
    col = len(key[0])  # col
    # result = [[0] * col] * row
    result = [[0] * row for _ in range(col)]
    for i in range(row):  # row ,col
        for j in range(col):
            result[j][row - j - 1] = key[i][j]  # 여긴걍 외워야할듯?
    return result


def check(answer):  # 아다리 들어 맞는지 확인하기
    lockLength = len(answer) // 3
    for i in range(lockLength, lockLength * 2):
        for j in range(lockLength, lockLength * 2):
            if answer[i][j] != 1:
                return False
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    # answer = [[0] * (n * 3)] * (n * 3)  # 맵을 *3으로 늘려놓고 돌리자
    answer = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            answer[i + n][j + n] = lock[i][j]

    for _ in range(4):
        key = rotate(key)
        for row in range(n * 2):  # answer를 위한 for문
            for col in range(n * 2):

                for i in range(m):  # key를 위한 for문
                    for j in range(m):
                        answer[row + i][col + j] += key[i][j]
                if check(answer):
                    return True
                for i in range(m):  # key를 위한 for문
                    for j in range(m):
                        answer[row + i][col + j] -= key[i][j]

    return False


lock = [[0, 0, 1], [0, 0, 2], [0, 0, 3]]
key = [[0, 0, 1], [0, 0, 2], [0, 0, 3]]
print(rotate(key))
