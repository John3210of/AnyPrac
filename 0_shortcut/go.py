############### 정규 표현식 활용법 # 정렬문제
import re
split_str = re.split(r"([0-9]+)", string)  # +는 기준으로나오는거 전부다 엮기
# asdfsdf123123asdfsdf 를 > asdfasdf, 123123, asdfasdf 로 나눠준다.
# https://whatisthenext.tistory.com/116 를 참고 하면 좋을듯?



############### input 시간 줄이면서 리스트로 입력 받기
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
        else:  # 첫 node일경우 들어감.
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



###################### 이진탐색
start=0
end = len(lst)
target=4
while start < end:
    mid = (start+end) // 2
    if lst[mid] < target:
        start = mid + 1
    elif lst[mid] > target:
        end = mid
    else:
        print(lst[mid])
        break
######################이진탐색 내장함수
import bisect
# bisect_left < 원하는 값이 여러개일경우, 가장 왼쪽에 있는
# 수의 idx를 반환한다.
def binary_search_builtin(nums, target):
    idx = bisect.bisect_left(nums, target)
    # idx == len(nums) 가능하기 떄문.
    if idx < len(nums) and nums[idx] == target:
        return idx
    else:  # 만약 없는경우 같거나 큰 가장 첫번째
        # 수의 idx를 반환한다.
        return -1



#######################2차원 배열 선언하기
# COLUM : 가로 길이
# ROW : 세로 길이
board = [[0 for i in range(COLUM)] for j in range(ROW)]
result = [[0] * row for _ in range(col)]
########################2차원 배열 zip하기
# https://juhee-maeng.tistory.com/entry/Python%EB%82%B4%EC%9E%A5%ED%95%A8%EC%88%98-zip%ED%95%A8%EC%88%98%EC%99%80-args-kwargs-%EB%9E%80
# https://codingdog.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-2%EC%B0%A8%EC%9B%90-%EB%B0%B0%EC%97%B4-%ED%9A%8C%EC%A0%84%EC%9D%84-1%EC%A4%84%EC%97%90-%EA%B5%AC%ED%98%84%ED%95%B4-%EB%B4%85%EC%8B%9C%EB%8B%A4
# zip함수에 *args를 인수로 넣을 수 있다.
# 리스트를 그냥 입력하지 말고, *를 붙여서 입력하면 col끼리 서로 엮어준다.
for i in zip(*alist):
    print(i)
# <output>
# (1, 4, 7)
# (2, 5, 8)
# (3, 6, 9)
# map과 zip함수를 사용해서 2차원 리스트를 transpose해주는것이 가능하지 않을까?
# 새로운 리스트에 transpose한 것을 할당해주고 싶다면?
blist = list(map(list, zip(*alist)))
# <output>
# blist
# [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
##################### 2차원 배열 회전하기
def rotated(a):
  n = len(a) # row
  m = len(a[0]) #col
  result = [[0]* n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result

