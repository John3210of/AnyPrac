# https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,root,root_leaf):
        if root is None:
            return
        elif root.left is None and root.right is None:
            root_leaf.append(root.val)
            return
        elif root.left and root.right is None:
            self.dfs(root.left,root_leaf)
        elif root.right and root.left is None:
            self.dfs(root.right,root_leaf)
        else:
            self.dfs(root.left,root_leaf)
            self.dfs(root.right,root_leaf)
        
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # leaf가 같은지를 확인하기
        # dfs로 leaf일때 lst에 추가하여 두 lst를 비교
        root1_leaf=[]
        root2_leaf=[]
        self.dfs(root1,root1_leaf)
        self.dfs(root2,root2_leaf)
        if root1_leaf==root2_leaf:
            return True
        return False