# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        a=deque()
        result=[]
        queue=deque([root])
        while queue:
            temp=0
            loop=len(queue)
            for i in range(loop):
                temp+=queue[i].val
                if queue[i].left:
                    queue.append(queue[i].left)
                if queue[i].right:
                    queue.append(queue[i].right)
            result.append(temp/loop)
            for i in range(loop):
                queue.popleft()
        return result