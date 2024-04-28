# https://leetcode.com/problems/middle-of-the-linked-list/

# 오답
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ListNode를 list형태로 만들어서 나머지 절반을 출력한다?
        # 리스트 길이//2 + 1 번째 부터 출력 
        # return 형이 listNode 여야 하나봐
        if head.next is None:
            return [head.val]
        linked_list=[]
        while head.next is not None:
            linked_list.append(head.val)
            print(head.next)
            head=head.next
        else:
            linked_list.append(head.val)
        output = linked_list[len(linked_list)//2:]
        return output

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ListNode를 list형태로 만들어서 나머지 절반을 출력한다?
        # 리스트 길이//2 + 1 번째 부터 출력 
        # return 형이 listNode 여야 하나봐
        head_coppied = head
        if head.next is None:
            return head
        count=0
        while head.next is not None:
            count+=1
            head=head.next
        else:
            count+=1
        for _ in range(count//2):
            head_coppied=head_coppied.next
        return head_coppied