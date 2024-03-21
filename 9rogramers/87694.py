# https://school.programmers.co.kr/learn/courses/30/lessons/87694 아이템줍기
graph = [[0 for _ in range(12)] for _ in range(12)]

rectangles = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]

for rec in rectangles:
    left_x,left_y,right_x,right_y=rec
    for i in range(left_y, right_y + 1):
        for j in range(left_x, right_x + 1):
            graph[i][j] = 1
print(graph)
# 상하좌우가 모두 1이면 가지말고, 모두1이 아닐때 가야함.
# 출발좌표 characterX,characterY / 도착좌표 itemX,itemY
characterX,characterY=1,3
itemX,itemY=7,8

# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
#  [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
#  [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
#  [0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0], 
#  [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0], 
#  [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
#  [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
#  [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
#  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

start=[characterY,characterX]
end=[itemY,itemX]

