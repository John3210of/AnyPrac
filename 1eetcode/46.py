# https://leetcode.com/problems/permutations/description/
import sys
sys.setrecursionlimit(100000)
class Solution:
    def dfs(self,visited,nums,atom,temp):
        if len(atom)==len(nums):
            temp.append(atom[:]) #shallow copy 때문에 
            return temp
        for i in range(len(nums)):
            if visited[i]==0:
                atom.append(nums[i])
                visited[i]=1
                self.dfs(visited,nums,atom,temp)
                atom.pop()
                visited[i]=0
        return temp

    def permute(self, nums: List[int]) -> List[List[int]]:
        # permutation 사용하지 않고 dfs
        # index를 각 한번씩만 사용하도록
        # 종료조건 : len(atom) == len(nums)
        # 2차원 리스트이므로 미리 for 한번 사용해서 읽기 편하게?
        answer=[]
        visited=[0]*len(nums)
        for i,num in enumerate(nums):
            temp=[]
            visited[i]=1
            answer.extend(self.dfs(visited,nums,[num],temp))
            visited[i]=0
        return answer
from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return [list(perm) for perm in permutations(nums)]