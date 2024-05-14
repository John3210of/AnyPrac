# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    from collections import deque
    def dfs(self,node,val_list):
        val_list.appendleft(node.val)
        if node.next is not None:
            self.dfs(node.next,val_list)
        return
    def dfs_str(self,node,val_str):
        val_str = str(node.val) + val_str
        if node.next is not None:
            val_str = self.dfs_str(node.next,val_str)
        return val_str
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 역순으로 정렬하려면 queue에 appendleft? 그냥 문자열로 하는게 낫겠네
        # string 은 immutable 하므로 return하는 형태로 dfs를 만들어야함
        # 메모리 최적화 어떻게 하면 좋을까
        l1_str=''
        l2_str=''
        l1_str = self.dfs_str(l1,l1_str)
        l2_str = self.dfs_str(l2,l2_str)
        answer = str(int(l1_str)+int(l2_str))[::-1]
        answer = list(map(int,answer))
        l3_list=[]
        for i in range(len(answer)):
            l3=ListNode(val=answer[i])
            l3_list.append(l3)
            if i>0:
                l3_list[i-1].next=l3
        return l3_list[0]
