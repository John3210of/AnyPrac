#leetcode 58번

class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class L_List:
    def __init__(self):
        self.head = None
        self.length = 0

    # 노드가 없을경우에 예외처리
    def isempty(self):
        return not bool(self.head)


    # 마지막 노드의 뒤에 입력
    def add_end(self, val):
        if not self.isempty():
            node = self.head
            while node.next:
                node = node.next
            node.next = (Node(val))
        else:
            self.head = Node(val)
        self.length += 1


    def deserial_linkedlist(self):  # 링크드리스트 역직렬화
        lst = []
        if not self.isempty():
            node = self.head
            while node:
                # print(node.val, end=' ')
                lst.append(int(node.val))
                node = node.next  ## 다음 노드로 넘어감
            lst.sort()
            print(lst)
            return lst
        else:
            print('list is empty')

        # 노드의 가장 앞에 입력
    def add_front(self, val):
        node = Node(val)
        if not self.isempty():
            node.next = self.head
            self.head = node
        else:  # 첫 node일경우 들어감.
            self.head = node
        self.length += 1


if __name__ == '__main__':
    linkedlist=L_List()

    linkedlist.add_front(4)
    linkedlist.add_end(2)
    linkedlist.add_end(3)
    linkedlist.add_end(1)
    linkedlist.deserial_linkedlist()


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# leetcode 제출용
# class Solution:
#     def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         lst = []
#         while head:
#             lst.append(head.val)
#             head = head.next
#         lst.sort()
#
#         answer = node = ListNode()
#
#         for i in lst:
#             node.next = ListNode(i)
#             node = node.next
#
#         return answer.next
#
