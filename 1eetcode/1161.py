# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    from collections import deque
    def bfs(self,root,node_val):
        if root is None:
            return
        queue=deque([root])
        while queue:
            level_sum=0
            level_len=len(queue)
            for _ in range(level_len):
                node = queue.popleft()
                level_sum+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            node_val.append(level_sum)            


    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # bfs 구현. 현재 queue에 있는 만큼 빼내고, 빼낸 노드의 sum(val)
        # queue에 들어가 있는 갯수가 현재 level에서 합을 구해야 하는 개수임
        # left, right가 존재할 경우에 queue에 추가하고, 꺼낸 node가 none일경우 무시함

        node_val=[]
        self.bfs(root,node_val)
        
        return node_val.index(max(node_val))+1 
# dfs 구현. depth를 파라미터로 넘기면서 dictionary에 합을 누적하는 방식?

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    from collections import defaultdict
    def dfs(self,node,depth_dic,depth):
        if node is None:
            return
        depth_dic[depth] += node.val
        self.dfs(node.left,depth_dic,depth+1)
        self.dfs(node.right,depth_dic,depth+1)

    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # dfs 로 depth를 dictionary화 하여 풀기
        depth_dic=defaultdict(int)
        self.dfs(root,depth_dic,1)
        max_val=float('-inf')
        for k,v in depth_dic.items():
            if v > max_val:
                max_key=k
                max_val=v
        return max_key
