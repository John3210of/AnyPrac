import sys
input = sys.stdin.readline

n,m = map(int, input().split())
a = [list(map(int,list(input().strip()))) for _ in range(n)]
b = [list(map(int,list(input().strip()))) for _ in range(n)]

def flip(row,col):
    for drow in range(3):
        for dcol in range(3):
            a[row+drow][col+dcol] = 1 - a[row+drow][col+dcol]
def solution():
    if a == b:
        return 0
    cnt = 0
    for row in range(n-2):
        for col in range(m-2):
            if a[row][col] != b[row][col]:
                flip(row,col)
                cnt += 1
            if a == b:
                return cnt
    return -1

print(solution())