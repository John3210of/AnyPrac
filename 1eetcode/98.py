
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.validate(root, float('-inf'), float('inf'))
    # 왼쪽 서브트리와 오른쪽 서브트리에 대해 재귀적으로 호출
    # 현재 노드의 값이 범위 밖에 있는지 확인
    # 왼쪽 서브트리는 현재 노드의 값보다 작아야 하며, 최대값은 현재 노드의 값이 됨
    # 오른쪽 서브트리는 현재 노드의 값보다 커야 하며, 최소값은 현재 노드의 값이 됨
    def validate(self, node, min_val, max_val):
        if not node:
            return True
        
        if node.val >= max_val or node.val <= min_val:
            return False
        
        return (self.validate(node.left, min_val, node.val) and
                self.validate(node.right, node.val, max_val))


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def check_bst(self, node: Optional[TreeNode],direction):
        root_val = node.val
        if direction == 'L':
            if not node.left.val < node.val:
                return False
            node=node.left
            if node.left is not None:
                if not node.left.val < root_val:
                    return False
                else:
                    self.check_bst(node,'L')
            if node.right is not None:
                if not root_val < node.right.val:
                    return False
                else:
                    self.check_bst(node,'R')

        elif direction == 'R':
            if not node.val < node.right.val:
                return False
            node=node.right
            if node.left is not None:
                if not node.left.val < root_val:
                    return False
                else:
                    self.check_bst(node,'L')
            if node.right is not None:
                if not root_val < node.right.val:
                    return False
                else:
                    self.check_bst(node,'R')
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # root val 기준으로 left의 val은 더 작고, right의 val은 더 커야함
        # left,right 가 존재하지 않는다면, 거기서 종료
        # left right 가 존재한다면, 값이 left, node, right 순인지 확인하여 아니면 false를 return
        # 항상 b tree가 아닐수도있음 왼쪽 오른쪽 나눠서 해야함
        if root.left is None and root.right is None:
            return True
        if root.left is not None:
            if self.check_bst(root,'L') is False:
                return False
        if root.right is not None:
            if self.check_bst(root,'R') is False:
                return False
        return True
child = TreeNode(val=1)
parent = TreeNode(val=1,left=child)

print(parent.val)
print(parent.left.val)
solution = Solution.isValidBST(parent)