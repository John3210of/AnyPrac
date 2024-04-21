# https://leetcode.com/problems/generate-parentheses/description/ 
import sys
sys.setrecursionlimit(100000)
class Solution:
    def dfs(self,n,start_count, end_count,atom,answer):
        if start_count==n and end_count==n:
            answer.append(atom)
            return answer
        if start_count >= end_count:
            if start_count < n:
                self.dfs(n,start_count+1, end_count,atom+"(",answer)
                self.dfs(n,start_count, end_count+1,atom+")",answer)
            else:
                self.dfs(n,start_count, end_count+1,atom+")",answer)
        return answer
        
    def generateParenthesis(self, n: int) -> List[str]:
        # 괄호쌍의 개수가 각각 n개가 될 때까지 dfs로?
        # 진행중인 )의 개수는 항상 (의 갯수 까지만 가능함
        # 종료조건 : (,) 의 개수가 모두 n이 될 때
        answer = []
        answer = self.dfs(n,1,0,'(',answer)
        return answer
