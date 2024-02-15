board =[["blue", "red", "orange", "red"], 
        ["red", "red", "blue", "orange"], 
        ["blue", "orange", "red", "red"], 
        ["orange", "orange", "red", "blue"]]

h=1 # 행
w=1 # 열

target_color = board[h][w]
moving_axis = [[-1,0],[1,0],[0,-1],[0,1]] #상 하 좌 우
count =0 
for i in range(4):
    if h+moving_axis[i][0] < 0 or w+moving_axis[i][1] < 0 or h+moving_axis[i][0] >= len(board) or w+moving_axis[i][1] >= len(board):
        pass
    else:
        if target_color == board[h+moving_axis[i][0]][w+moving_axis[i][1]]:
            count += 1
print('count',count)

