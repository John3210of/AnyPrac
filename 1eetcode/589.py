# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def dfs(self,node,answer):
        answer.append(node.val)
        if len(node.children) == 0:
            return answer
        for child in node.children:
            self.dfs(child,answer)
        return answer
    def preorder(self, root: 'Node') -> List[int]:
        # 트리 순회 dfs
        # 종료조건 : children이 없을경우
        # depth우선 탐색하여 answer에 append
        answer=[]
        if root is None: # 이거 때문에 애먹음
            return []
        answer = self.dfs(root,answer)
        return answer