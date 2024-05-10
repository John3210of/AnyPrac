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

triangle=[    [7], 
             [3, 8], 
            [8, 1, 0], 
           [2, 7, 4, 4], 
          [4, 5, 2, 6, 5]]

triangle_dp=[triangle[0]]
# triangle 1번째 열부터 순회하면서 값을 채워나갈거임.
# 현재 라인의 모든 col을 순회하며 존재한다면 바로위의값과 그 이전col의 값을 더한값중에 더 큰값
# 벽일경우 col==0 or col==len(current_tri)-1 >> 첫번째값과 마지막값
# 벽이 아닐경우 col-1 값과 col 값중 max인 값
for row in range(1,len(triangle)):
    current_tri=triangle[row]
    prev_tri=triangle[row-1]
    temp_row=[0]*len(current_tri)
    for col in range(len(current_tri)):# row=1,col=0
        if col==0:
            temp_row[col]=current_tri[0]+prev_tri[0]
        elif col==len(current_tri)-1:
            temp_row[-1]=current_tri[-1]+prev_tri[-1]
        else:
            temp_row[col]=max(prev_tri[col-1],prev_tri[col])+current_tri[col]
    triangle[row] = temp_row
print(triangle)
print(max(triangle[-1]))