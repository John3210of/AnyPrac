# https://school.programmers.co.kr/learn/courses/30/lessons/43105 정수 삼각형
triangle=[[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
dp = [triangle[0][0]]

# 삼각형의 각 줄을 순회하면서 최대값을 구함
for i in range(1, len(triangle)):
    row = triangle[i]
    temp = [0] * len(row)
    for j in range(len(row)):
        left_up = dp[j - 1] if j - 1 >= 0 else -1
        right_up = dp[j] if j < len(dp) else -1
        # 두 경우 중 더 큰 값을 현재 위치의 값과 더함
        temp[j] = max(left_up, right_up) + row[j]
    dp = temp

# 맨 아래 줄까지의 최대값이 저장된 dp 리스트의 최댓값을 반환
result = max(dp)
print(result)