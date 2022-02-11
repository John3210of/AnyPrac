# 상수 n!에 대하여 나머지가 없게하는 상수 k의 i승을 구하여라.
# import sys
#
# input = sys.stdin.readline
# t = int(input())
# lst = []
# for _ in range(t):
#     lst.append(list(map(int, input().split())))
# k_lst = []
# j = 1
# while True:
#     if lst[0][1] ** j > lst[0][0] / 2:
#         print(k_lst,j)
#         break
#     k_lst.append(lst[0][1] ** j)
#     j += 1
#
# for leg in range(len(lst)):
#     temp = 1
#     n_fac = 1
#     for i in range(1, lst[leg][0] + 1):  # n! 구하기  #lst[leg][0] = n , lst[leg][1] = k
#         n_fac *= i
#
#     for j in range(1, lst[leg][0] + 1):  # j = 1 2 3 4 5
#         if n_fac % lst[leg][1] != 0:
#             continue
#         if n_fac % (lst[leg][1] ** j) == 0:
#             if j > temp:
#                 temp = j
#     print(temp)

# n! 에는 n , n-1, ... , 2,1 까지의 수가 있다. 당연히 소수가 되어야한다.
# 5! = 120 =5 4 3 2 1 ,,k=> 5 4 3 2 1 중에 하나. 2의 x승이 팩토리얼의 조합중에 하나여야한다.


#
#
#
#
#
#
#
#
#
#
#
# # 상수 n!에 대하여 나머지가 없게하는 상수 k의 i승을 구하여라.
import sys

input = sys.stdin.readline
t = int(input())
lst = []
for _ in range(t):
    lst.append(list(map(int, input().split())))

for leg in range(len(lst)):
    temp = 1
    n_fac = 1
    for i in range(1, lst[leg][0] + 1):  # n! 구하기  #lst[leg][0] = n , lst[leg][1] = k
        n_fac *= i

    for j in range(1, lst[leg][0] + 1):  # j = 1 2 3 4 5
        if n_fac % lst[leg][1] != 0:
            continue
        if n_fac % (lst[leg][1] ** j) == 0:
            if j > temp:
                temp = j
    print(temp)
#
# # n! 에는 n , n-1, ... , 2,1 까지의 수가 있다. 당연히 소수가 되어야한다.
# # 5! = 120 =5 4 3 2 1 ,,k=> 5 4 3 2 1 중에 하나. 2의 x승이 팩토리얼의 조합중에 하나여야한다.
