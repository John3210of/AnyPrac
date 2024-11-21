from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        '''
        [[-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,35,-1,-1,13,-1],
        [-1,-1,-1,-1,-1,-1],
        [-1,15,-1,-1,-1,-1]]
        # 라벨링이 되어있다.
        한번에 사다리를 2개씩 탈 수는 없다.
        최소 1칸, 최대 6칸을 이동 가능하다.
        n^2 까지 가는 최소 이동횟수
        dfs로 1~6칸까지 이동시키면서 시뮬레이션하다가 가장 먼저 n^2으로 갔을때의 이동횟수를 리턴
        '''
        n = len(board)
        board_label = deque()
        for i in range(n):
            start = 1 + i*n
            temp = [start + j for j in range(n)]
            if i%2 == 1:
                temp = temp[::-1]
            board_label.appendleft(temp)
        dic = {}
        for row in range(len(board_label)):
            for col in range(len(board_label[0])):
                dic[board_label[row][col]] = board[row][col]
        min_count = n**3
        def dfs(start, count):
            nonlocal min_count
            # 종료조건 : n^2이 되었을때
            if count > n**2:
                return
            if start >= n**2:
                if min_count > count:
                    min_count = count
                return
            if count >= min_count:
                return
            for i in range(1,7):
                if start+i > n**2:
                    break
                elif dic[start+i] == start:
                    pass
                elif dic[start+i] != -1:
                    dfs(dic[start+i], count+1)
                else:
                    dfs(start+i, count+1)
        dfs(1, 0)
        return min_count if min_count <= n**2 else -1
    
'''
edge case
# 홀수개일때 처리 부족
board =
[[-1,4,-1],[6,2,6],[-1,3,-1]]

# 절대 완주할수없을경우
board =
[[1,1,-1],[1,1,1],[-1,1,1]]

# 시간초과
Time Limit Exceeded
70 / 215 testcases passed
Last Executed Input
Use Testcase
board =
[[-1,-1,-1,13,123,-1,-1,-1,-1,37,-1,-1],[-1,-1,-1,-1,-1,-1,123,-1,-1,-1,-1,-1],[123,-1,-1,-1,79,70,-1,-1,17,-1,-1,103],[-1,-1,120,-1,101,-1,2,72,-1,-1,-1,-1],[-1,71,77,-1,-1,-1,-1,35,-1,-1,-1,-1],[-1,-1,98,-1,-1,-1,-1,-1,-1,99,-1,-1],[83,-1,108,27,-1,-1,113,-1,-1,-1,79,-1],[28,-1,-1,-1,57,14,-1,48,-1,-1,-1,-1],[-1,-1,-1,-1,16,115,-1,46,-1,-1,-1,-1],[-1,-1,4,-1,-1,-1,-1,-1,-1,-1,-1,-1],[94,-1,116,-1,-1,-1,39,100,-1,-1,16,-1],[-1,94,-1,-1,53,-1,-1,-1,-1,-1,-1,-1]]
'''

# bfs로 풀면
from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        label = []
        for i in range(n):
            row = board[n - 1 - i]
            if i % 2 == 0:
                label.extend(row)
            else:
                label.extend(row[::-1])
        visited = set()
        queue = deque([(1, 0)])
        while queue:
            pos, moves = queue.popleft()
            if pos >= n * n:
                return moves
            for i in range(1, 7):
                next_pos = pos + i
                if next_pos > n * n:
                    break
                if label[next_pos - 1] != -1:
                    next_pos = label[next_pos - 1]
                if next_pos not in visited:
                    visited.add(next_pos)
                    queue.append((next_pos, moves + 1))
        return -1