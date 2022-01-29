# leetcode 21. 두정렬리스트 병합
# 두 개의 정렬된 연결 목록 list1과 list2의 헤드가 제공됩니다.
# 두 개의 목록을 하나의 정렬된 목록으로 병합합니다. 목록은 처음 두 목록의 노드를 연결하여 만들어야 합니다.
# 병합된 연결 목록의 헤드를 반환합니다.
# https://velog.io/@woga1999/%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9C%BC%EB%A1%9C-%EA%B5%AC%ED%98%84%ED%95%98%EB%8A%94-%EB%A7%81%ED%81%AC%EB%93%9C-%EB%A6%AC%EC%8A%A4%ED%8A%B8
# https://koosco.tistory.com/80

# 노드 선언
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# 리스트 선언
class L_List:
    def __init__(self):
        self.head = None
        self.length = 0

    # 노드가 없을경우에 예외처리
    def isempty(self):
        return not bool(self.head)

    # 현재 노드의 앞에 입력
    def add_front(self, val):
        node = Node(val)
        if not self.isempty():
            node.next = self.head
            self.head = node
        else:       #첫 node일경우 들어감.
            self.head = node
        self.length += 1

    # 현재 노드의 뒤에 입력
    def add_end(self, val):
        if not self.isempty():
            node = self.head
            while node.next:
                node = node.next
            node.next = (Node(val))
        else:
            self.head = Node(val)
        self.length += 1

    # 노드 원하는 위치로 삽입해주기
    def insert(self, pos, val):
        if not self.isempty():
            if pos == 0:
                self.add_front(val)

            elif pos == self.length:
                self.add_end(val)

            else:
                node = self.head
                cnt = 0
                while pos > 0 and pos < self.length:
                    if cnt == pos - 1:
                        new_node = Node(val)
                        node.next = new_node
                        break
                    node = node.next
                    cnt += 1
                self.length += 1

    def printnode(self):
        if not self.isempty():
            node = self.head
            while node:
                # print(node.val, end=' ')
                print(int(node.val))
                node = node.next
            # print()
        else:
            print('list is empty')



## value를 임시저장소에 받아서 sorted하고 다시 linked list를 만든다?
## 합친다.. 잇는다.. 무엇이 범용성 있을지?
# 풀어야 하는문제가 정렬된 리스트를 다시 정렬하면서 병합.
# 리스트의 tail과 head를 뒤집는다.
# 공간복잡도 O(1), 시간복잡도 O(n)을 가지고 노드를 재구성 >> 따로 저장시키지 않으면서 n번 조사하는것만으로 알고리즘이 끝나야한다.

    # def sorted(self):
    #     data=[]
    #     node = self.head
    #     for i in range(0, self.length):
    #         data.append(node.val)
    #         # print(node.val)
    #         node = node.next
    #
    #     print(data)

    # def mergesorted(self,list1:Node,list2:Node):




if __name__ == '__main__':
    list = L_List()
    list2 = L_List()

    list.add_front(1)
    list.add_end(2)
    list.add_end(4)
    list.insert(1,5)
    list.printnode()


    #
    #
    # list2.add_front(1)
    # list2.add_end(3)
    # list2.add_end(4)
    # list2.printnode()


