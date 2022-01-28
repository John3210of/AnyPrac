# 널리 잘 알려진 자료구조 중 최소 힙이 있다.
# 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

# 1. 배열에 자연수 x를 넣는다.
# 2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
# 프로그램은 처음에 비어있는 배열에서 시작하게 된다.

# example

# lst=none ,pop:0>  lst=[12345678] > lst=[12345678,1,2] > pop:1 , lst=[12345678,2]
# >pop:2, lst=[12345678] > pop:12345678, lst=none > lst=none,pop:0
# import sys
# n = int(sys.stdin.readline())
# x=[]
# for i in range(n):
#     s=int(sys.stdin.readline())
#     x.append(s)

##################################
# 1. n만큼 input 받는다.
# 2-1. x가 0일 경우 output=>min(lst)를 pop
# 2-2. x가 0이 아닐경우 lst.append(x)

# temp input
# n = 9
# x = [0, 12345678, 1, 2, 0, 0, 0, 0, 32]
# from collections import deque
# import sys
# n = int(sys.stdin.readline())
# x=[]
# for i in range(n):
#     s=int(sys.stdin.readline())
#     x.append(s)
# lst = []
# queue = deque(x)
#
# while queue:
#     temp = queue.popleft()
#     if temp != 0:
#         lst.append(temp)
#     else:
#         if len(lst) == 0:
#             print('0')
#         else:
#             tmp = min(lst)
#             res = lst.pop(lst.index(tmp))
#             print(res)
############################

import sys
import heapq
n = int(sys.stdin.readline())
x = []
for i in range(n):
    s = int(sys.stdin.readline())
    x.append(s)

heap=[]

for i in x:
    if i!=0:
        heapq.heappush(heap,i)
    else:
        if len(heap)==0:
            print('0')
        else:
            res=heapq.heappop(heap)
            print(res)



