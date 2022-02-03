############### 정규 표현식 활용법 # 정렬문제
import re

split_str = re.split(r"([0-9]+)", string)  # +는 기준으로나오는거 전부다 엮기
# asdfsdf123123asdfsdf 를 > asdfasdf, 123123, asdfasdf 로 나눠준다.
# https://whatisthenext.tistory.com/116 를 참고 하면 좋을듯?


############### input 시간 줄이면서 list로 받기
import sys

input = sys.stdin.readline
home = list(map(int, input().split()))
# 스플릿의 경우 .strip() 붙여주면 \n을 방지할수 있다.


############### 링크드리스트 구현

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
            print('empty')
