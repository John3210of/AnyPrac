# 단일 연결 목록의 헤드가 주어지면 삽입 정렬을 사용하여 목록을 정렬하고 정렬된 목록의 헤드를 반환합니다.
#
# 삽입 정렬 알고리즘의 단계:
#
# 삽입 정렬은 반복될 때마다 하나의 입력 요소를 사용하고 정렬된 출력 목록을 늘립니다.
# 각 반복에서 삽입 정렬은 입력 데이터에서 하나의 요소를 제거하고,
# 정렬된 목록 내에서 해당 요소가 속한 위치를 찾아 거기에 삽입합니다.
# 입력 요소가 남아 있지 않을 때까지 반복됩니다.
# 다음은 삽입 정렬 알고리즘의 그래픽 예입니다.
# 부분적으로 정렬된 목록(검정색)은 처음에 목록의 첫 번째 요소만 포함합니다.
# 하나의 요소(빨간색)가 입력 데이터에서 제거되고 각 반복과 함께 정렬된 목록에 제자리에 삽입됩니다.

# 노드 선언

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

    # 노드의 가장 앞에 입력
    def add_front(self, val):
        node = Node(val)
        if not self.isempty():
            node.next = self.head
            self.head = node
        else:  # 첫 node일경우 들어감.
            self.head = node
        self.length += 1

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
            return lst
        else:
            print('list is empty')


def insertionsort(lst):
    # 0번째 요소는 이미 정렬되어있으니, 1번째 ~ lst(len)-1 번째를 정렬하면 된다.
    for cur in range(1, len(lst)):
        for delta in range(1, cur + 1):
            cmp = cur - delta  # delta 만큼 역순으로 비교하고 swap
            if lst[cmp] > lst[cmp + 1]:
                lst[cmp], lst[cmp + 1] = lst[cmp + 1], lst[cmp]
            else:
                break
    return lst


lst = [4, 2, 1, 3]

if __name__ == '__main__':
    Linklist = L_List()
    for i in range(len(lst)):
        Linklist.add_end(lst[i])
    #[4 > 2 > 1 > 3]
    de = []
    de = Linklist.deserial_linkedlist()
    #[4,2,1,3]
    answer = insertionsort(de)
    print(answer)



# 삽입정렬이란? 바운더리를 넓혀가면서
# 내부적으로는 가장 오른쪽 index부터 0번까지 비교하면서 정렬하는것
# 일단 이어 붙여놓고 val만 swap할지. => 삽입 정렬만
# node를 떼서 붙일지. => linked list 까지


