# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def get_max_path(self, node: TreeNode, max_path_sum: list) -> int:
        if not node:
            return 0

        # 왼쪽과 오른쪽 하위 트리에서 최대 경로 합을 구함
        left_max_sum = max(self.get_max_path(node.left, max_path_sum), 0)
        right_max_sum = max(self.get_max_path(node.right, max_path_sum), 0)

        # 현재 노드를 포함하는 경로의 최대 합 계산
        current_max_path_sum = node.val + left_max_sum + right_max_sum
        
        # 전체 최대 경로 합 갱신
        max_path_sum[0] = max(max_path_sum[0], current_max_path_sum)

        # 현재 노드에서 시작하는 경로 중 최대 합 반환
        return node.val + max(left_max_sum, right_max_sum)
        
    def maxPathSum(self, root: TreeNode) -> int:
        max_path_sum = [float('-inf')]  # 최대 경로 합을 저장할 리스트 초기화
        self.get_max_path(root, max_path_sum)
        return max_path_sum[0]

root2 = TreeNode(-10)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.right.left = TreeNode(15)
root2.right.right = TreeNode(7)
sol = Solution()
print(sol.maxPathSum(root2))  # 출력: 42

