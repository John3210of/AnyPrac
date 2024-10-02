# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Binary search tree 에서 k번째 원소를 찾는법
        while root:
            val = root.val
            root = root.left
        return k+val-1
        