from itertools import permutations

def generate_permutations(s):
    # 문자열 s의 모든 순열을 생성하여 리스트로 반환
    return [''.join(permutation) for permutation in permutations(s)]

# 예시
s = "abc"
all_permutations = generate_permutations(s)
print(all_permutations)

from itertools import permutations
def generate_permutations(s, length):
    # 문자열 s의 길이가 length인 모든 순열을 생성하여 리스트로 반환
    return [''.join(permutation) for permutation in permutations(s, length)]
s = "abc"
n = len(s)
all_permutations = []
for length in range(1, n + 1):
    all_permutations.extend(generate_permutations(s, length))

def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def convert_to_base_n(number, base):
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        number, remainder = divmod(number, base)
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(remainder - 10 + ord('A')) + result
    return result

def is_prime(number): # 소수판별
    if number == 2:
        return True
    if number <= 1:
        return False
    if number%2 ==0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True

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
start = 0
end = len(lst)
target = 4
while start < end:
    mid = (start + end) // 2
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
    n = len(a)  # row
    m = len(a[0])  # col
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


#######################[Python] 두 리스트(배열) 각 요소들의 값 더하기
#
# 1. list comprehension 을 사용하기
[list1[i] + list2[i] for i in range(len(list1))]
# 2. zip 함수를 사용하기
[x + y for x, y in zip(list1, list2)]

###########################다익스트라
import heapq

INF = int(1e9)


def dijkstra_pq(graph, start):
    N = len(graph)
    dist = [INF] * N

    q = []
    # 튜플일 경우 0번째 요소 기준으로 최소 힙 구조.
    # 첫 번째 방문 누적 비용은 0이다.
    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        # 누적 비용이 가장 작은 녀석을 꺼낸다.
        acc, cur = heapq.heappop(q)

        # 이미 답이 될 가망이 없다.
        if dist[cur] < acc:
            continue

        # 인접 노드를 차례대로 살펴보며 거리를 업데이트한다.
        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist


# 소수구하기
def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i + i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    return [i for i in range(2, n) if sieve[i] == True]


# 소수구하기 2 백준 4948
prime = [True] * 123457 * 2  # 범위만큼 전부 구해놓기
prime[1] = False
for i in range(2, len(prime)):
    if prime[i]:
        for j in range(i * 2, len(prime), i):  # 2i, 3i, 4i로 끝까지 가라.
            prime[j] = False
while True:
    n = int(input())
    if n == 0:
        break
    print(sum(prime[n + 1:2 * n + 1]))

    # 부분집합 구하기
    for i in lst:  # res=[[]]
        size = len(res)
        for j in range(size):
            res.append(res[j] + [i])

# 문자열 n개씩 잘라서 list화 하기기

seq = '12312312312312'
length = 3
[seq[i:i + length] for i in range(0, len(seq), length)]

# result
['123', '123', '123', '123', '12']  ##전부다 필요
#############
seq = '12312312312312'
length = 3
[''.join(x) for x in zip(*[list(seq[z::length]) for z in range(length)])]

# result
['123', '123', '123', '123']  # 잘린 애만 필요

# 딕셔너리
d.get(x,0) > x가 없으면 0으로 추가
for key,val in d.items() > 딕셔너리 key,val값 볼 수 있음
#set은 hashtable로 이루어져 있다.
s=set(lost) & set(reserve) #교집합을 의미

#형태 변환 str > int map list
numbers2=list((map(str,numbers)))

