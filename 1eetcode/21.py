# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 병합정렬
        # root1, root2 중에 더 작은 값으로 시작.
        # 시작한곳의 next와 시작하지 않은곳의 값을 비교하여 더 작은 값을 넣는다.
        answer = []
        while list1 or list2:
            if list2 is None:
            # if list1 is not None and list2 is None:
                answer.append(list1.val)
                list1 = list1.next
            elif list1 is None:
            # elif list2 is not None and list1 is None:
                answer.append(list2.val)
                list2 = list2.next
            elif list1.val <= list2.val:
                # node.val = list1.val
                answer.append(list1.val)
                list1 = list1.next
            elif list1.val > list2.val:
                # node.val = list2.val
                answer.append(list2.val)
                list2 = list2.next
        for i in range(len(answer)):
            node = ListNode(val=answer[-1-i])

        
        return node