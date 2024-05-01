# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # 리스트로 만들어서 정렬후에 +1 자리와 비교?
    # inorder를 사용할 시에 오름차순 정렬이 된다.
    # 차이값을 계산하기위해 노드를 2개이상 발견했는지에 대한 판단 필요
    def __init__(self):
        self.init = False
        self.prev = None
        self.min_val = float('inf')
    def inorder(self, root: TreeNode):
        if root is None:
            return None
        self.inorder(root.left)
        if self.init:
            self.min_val = min(self.min_val, root.val - self.prev)
        else:
            self.init = True
        self.prev = root.val
        self.inorder(root.right)
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.inorder(root)
        return self.min_val