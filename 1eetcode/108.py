# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sorted_array_to_BST(self,nums):
        if not nums:
            return None
    
        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sorted_array_to_BST(nums[:mid])
        root.right = self.sorted_array_to_BST(nums[mid+1:])
        
        return root

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # 반반 나눠서 left right로 dfs
        return self.sorted_array_to_BST(nums)