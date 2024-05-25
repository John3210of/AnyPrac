'''
❓ 3장 함수
    refactoring boj 14502.py
- 한가지만 해야 한다?
- 최대한 서술적인 이름을 써야한다?
- 함수에서 인수가 많을수록 안좋다 > 그럼 어떻게 해 글로벌 변수는 쓰면 엄청 불편한데
- 내려가며 읽히는 함수의 순서
- *args, *kargs 를 쓰는 python은?

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

> 9

'''
import sys
import copy
from collections import deque
class Lab:
    def __init__(self,graph):
        self.graph=graph

    def build_walls_and_evaluate(self, walls, max_area):
        if walls == 3:
            return self._calculate_safe_area(max_area)
        else:
            return self._place_wall_and_backtrack(walls, max_area)
        
    def _place_wall_and_backtrack(self, walls, max_area):
        for row in range(len(self.graph)):
            for col in range(len(self.graph[0])):
                if self.graph[row][col] == 0:
                    self.graph[row][col] = 1
                    max_area = self.build_walls_and_evaluate(walls + 1, max_area)
                    self.graph[row][col] = 0
        return max_area

    def _calculate_safe_area(self, max_area):
        temp_graph = self._spread_virus()
        temp_safe_area=0
        for i in range(len(temp_graph)):
            temp_safe_area += temp_graph[i].count(0)
        return max(temp_safe_area, max_area)

    def _spread_virus(self):
        drow=[1,-1,0,0]
        dcol=[0,0,1,-1]
        temp_graph=copy.deepcopy(self.graph)
        infected_q=deque()
        for row in range(len(temp_graph)):
            for col in range(len(temp_graph[0])):
                if temp_graph[row][col] == 2:
                    infected_q.append([row,col])
        while infected_q:
            row, col = infected_q.popleft()
            for i in range(4):
                next_row=row+drow[i]
                next_col=col+dcol[i]
                if self._is_enable_axis(next_row,next_col,temp_graph):
                    temp_graph[next_row][next_col]=2
                    infected_q.append([next_row,next_col])
        return temp_graph
    
    def _is_enable_axis(self,row,col,graph):
        if 0 <= row < len(graph) and 0 <= col < len(graph[0]) and graph[row][col]==0:
            return True
        else:
            return False

if __name__ == "__main__":

    sys.setrecursionlimit(100000)
    input = sys.stdin.readline
    n,m = map(int,input().split())
    graph=[]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    lab=Lab(graph)
    print(lab.build_walls_and_evaluate(0,0))

    