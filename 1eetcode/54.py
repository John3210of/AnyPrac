class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 시계방향 회전, 끝을만나거나 이미 방문한곳일경우 방향을 바꿔서 진행시킨다.
        # 방향은 우,하,좌,상 순서
        m,n = len(matrix),len(matrix[0])
        answer_length = m*n
        visited = [[False for _ in range(n)] for _ in range(m)]
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        flag = 0
        row,col = 0,0
        visited[row][col]= True
        answer=[matrix[0][0]]
        while len(answer) < answer_length:
            next_row = direction[flag][0] + row
            next_col = direction[flag][1] + col
            if 0 <= next_row < m and 0 <= next_col < n and not visited[next_row][next_col]:
                visited[next_row][next_col]=True
                row = next_row
                col = next_col
                answer.append(matrix[row][col])
            else:
                flag = (flag+1)%4
        return answer