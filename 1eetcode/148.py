# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 하나씩 value 꺼내서 heap 형태로 만들고 heappop으로 뽑아내기?
        if head is None or head.next is None:
            return head
        max_heap=[]
        while head:
            heapq.heappush(max_heap,-head.val)
            head=head.next
        # max heap으로 해야대나?
        node = ListNode(val=-heapq.heappop(max_heap),next=None)
        while max_heap:
            node = ListNode(val=-heapq.heappop(max_heap),next=node)
        return node