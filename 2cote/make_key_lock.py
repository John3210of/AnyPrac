def rotated(key):  # 90도 회전하기
    row = len(key)  # row
    col = len(key[0])  # col

    result = [[0] * row for _ in range(col)]

    for i in range(row):
        for j in range(col):
            result[j][row - i - 1] = key[i][j]

    return result


def search(key, lock, start_row, start_col):
    length = (2 * len(key)) + len(lock)  # 확장시킬 한 변의 길이
    background = [[0] * length for _ in range(length)]  # 확장시킨 2차원 배열
    end = len(key) + len(lock)

    for row in range(len(key)):
        for col in range(len(key[0])):
            background[row + start_row][col + start_col] = key[row][col]

    for row in range(len(key), end):
        for col in range(len(key), end):
            background[row][col] += lock[row - len(key)][col - len(key)]
            if background[row][col] != 1:
                return False

    return True


def solution(key, lock):
    end = len(key) + len(lock)
    for k in range(4):
        for row in range(end):
            for col in range(end):
                start_row = row
                start_col = col
                if search(key, lock, start_row, start_col) == True:
                    return True
        key = rotated(key)

    return False


# 1. 회전하는 매커니즘

# 2. 상하좌우로 가는 매커니즘 >> pop하고 0을 appendleft하거나 popleft하고 0을 append
# 3. ** lock의 0이 있는 패턴을 저장해 **
#      key에서 1이 있는 패턴이 위에서 구한 패턴과 같은지 봐. 없으면 회전시켜봐.
#      회전3번 해도 없으면 false를 리턴해.

# 4.  패턴이 존재한다면 두 이차원 배열끼리 포개서 합쳐.
#      만약 포개서 합칠때 2가 있다면 다시 회전해서 패턴을보고, 끝까지 없다면 다시 false를 리턴해.
#

def solution(key, lock):
    def rotated(key):  # 90도 회전하기
        row = len(key)  # row
        col = len(key[0])  # col

        result = [[0] * row for _ in range(col)]

        for i in range(row):
            for j in range(col):
                result[j][row - i - 1] = key[i][j]

        return result

    def find_pattern(key, lock, cnt):

        getpattern
        by
        lines

        if cnt > 3:
            return False

        if key_pattern == lock_pattern:
            sum_cover(key, lock)
        else:
            cnt += 1
            find_pattern(rotated(key), lock)

    def sum_cover(key, lock):
        if is_two_exist:
            return False
        else:
            return True

    cnt = 0
    return find_pattern(key, lock, cnt)
#
#
#
#     # key2 = rotated(key)
#     # key3 = rotated(rotated(key))
#     # key4 = rotated(rotated(rotated(key)))
#     # print(key)
#     # print(key2)
#     # print(key3)
#     # print(key4)
#     # return True
#
#
# key = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# print(solution(key))
#
# # lock = [
# #     [1, 1, 1, 1],
# #     [1, 1, 0, 1],
# #     [1, 0, 1, 1],
# #     [1, 0, 1, 1]
# # ]
# #
# # board = [[0 for i in range(len(lock[0]))] for j in range(len(lock))]
