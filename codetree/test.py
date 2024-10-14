# # dp
# n = int(input())
# triangle=[]
# for _ in range(n):
#     temp = list(map(int,input().split()))
#     triangle.append(temp)
# # 삼각형 dp 왼쪽 가운데 오른쪽으로 갈건데, 더 큰값으로 바꿔줄거임
# # 왼쪽으로 못가는 애는 0번, 오른쪽으로 못가는애는 -1번
# dp=[[0 for _ in range(j)] for j in range(1,2*n,2)]
# dp[0][0] = triangle[0][0]
# if n == 1:
#     print(dp[0][0])
# else:
#     dp[1][0] = dp[0][0] + triangle[1][0]
#     dp[1][1] = dp[0][0] + triangle[1][1]
#     dp[1][2] = dp[0][0] + triangle[1][2]
#     for row in range(2,len(triangle)):
#         for col in range(2*row+2):
#             if col == 0:
#                 dp[row][col] = dp[row-1][col] + triangle[row][col]
#             elif col == 1:
#                 dp[row][col] = max(dp[row-1][0], dp[row-1][1]) + triangle[row][col]
#             elif col == 2*row:
#                 dp[row][col] = max(dp[row-1][-1],dp[row-1][-2]) + triangle[row][col]
#             elif col == 2*row+1:
#                 dp[row][col] = dp[row-1][-1] + triangle[row][col]
#             else:
#                 dp[row][col] = max(dp[row-1][col-1],dp[row-1][col],dp[row-1][col+1]) + triangle[row][col]
# for i in range(dp):
#     for j in range(dp[i]):
#         print(dp[i][j],end = ' ')
#     print()

'''
3
1
1 3 5
2 3 2 4 6
2 1 5 2 7 2 4

'''

n = int(input())  # 삼각형의 크기 (높이)
triangle = []

# 삼각형 입력 받기
for _ in range(n):
    triangle.append(list(map(int, input().split())))

# DP 테이블 초기화 (삼각형과 같은 크기)
dp = [[0] * len(triangle[i]) for i in range(n)]

# DP의 첫 번째 값은 삼각형의 꼭대기 값
dp[0][0] = triangle[0][0]

# DP 테이블 채우기
for i in range(1, n):
    for j in range(len(triangle[i])):
        # 왼쪽 대각선 위에서 올 수 있는 값
        left_up = dp[i-1][j-1] if j-1 >= 0 else float('-inf')
        
        # 바로 위에서 올 수 있는 값
        mid_up = dp[i-1][j] if j < len(triangle[i-1]) else float('-inf')
        
        # 오른쪽 대각선 위에서 올 수 있는 값
        right_up = dp[i-1][j+1] if j+1 < len(triangle[i-1]) else float('-inf')

        # 가능한 값 중 최댓값을 선택하고 현재 값과 더함
        dp[i][j] = triangle[i][j] + max(left_up, mid_up, right_up)

# 마지막 줄에서 최대값을 찾음
for i in dp:
    print(i)
