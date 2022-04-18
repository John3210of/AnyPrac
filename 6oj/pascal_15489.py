import sys

input = sys.stdin.readline
r, c, w = map(int, input().split())
n = r - 1
m = c - 1
pascal = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1],
          [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1]]
res = 0
for width in range(w):
    for last in range(width+1):
        res += pascal[n + width][m + last]
print('res', res)


# print('width : ', width)
# print('last : ', last)
# print('value : ', pascal[n + width -1][m + last])
# print("*******************************")
# n m
# n+1 m , n+1,m+1
# n+w,m, n+w,m+1 .... n+w,m+w
# r cw
# 3 1 // 4 1 ,4 2 // 5 1, 5 2, 5 3 // 6 1, 6 2, 6 3, 6 4
# print(pascal[r-1][c-1])
# print("pascal", pascal)
# print("r,c,w", r, c, w)
