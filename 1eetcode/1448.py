# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # 모든 노드를 방문하면서, gte 인 노드의 수를 return
        # 트리 완전 탐색
        # 자기 경로상에 값이 더 큰값이 없어야함
        count=0
        def visit_node(node,max_val):
            nonlocal count
            if node.val >= max_val:
                max_val = node.val
                count+=1
            if node.left is not None:
                visit_node(node.left,max_val)
            if node.right is not None:
                visit_node(node.right,max_val)
        if root.val is not None:
            visit_node(root,root.val)
        return count
    