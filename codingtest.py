import re
# 유형 1의 경우 010으로 시작하며 -4자리-4자리 숫자 존재한다.
# 유형 2의 경우 010으로 시작하며 8자리 숫자 존재한다.
# 유형 3의 경우 +82-10-4자리-4자리 숫자 존재한다.
p = '010-5108-1201'
p = re.compile()

answer = 0
return answer

# #######################################
# # 실행시간 체크 모듈
# import math
# import time
#
# start = time.time()
# math.factorial(100000)
# end = time.time()
# print(f"{end - start:.5f} sec")
# #######################################
#
#
#
#
#
#
#
#
# str = input()
#
#                         #왜 palins 와 palins2를 나누어서 진행했는지 설명해주시면 좋을것 같습니다.
# palins = []
# palins2 = []
#
# for i in range(len(str)):
#     palin_count = 0
#     for j in range(len(str)-i):
#         if i-j >= 0 and i+j < len(str):
#             if str[i-j] == str[i+j]:
#                 palin_count = palin_count + 1       #count의 변화를 아까처럼 한번 보여주시면 이해가 더 쉬울것 같습니다.
#             else: break
#
#     palins.append(palin_count)
#
# ## i와 i+1을 비교
# for i in range(len(str)-1):
#     palin_count = 0
#     for j in range(len(str)-1-i):
#         if i-j >= 0 and i+j+1 < len(str):
#             if str[i-j] == str[i+j+1]:
#                 palin_count = palin_count + 1
#             else: break
#     palins2.append(palin_count)
#
# ##출력부
# if max(palins) < max(palins2):
#     middleidx = palins2.index(max(palins2))
#     temp = max(palins2)
#     print(str[middleidx-temp+1:middleidx+temp+1])
#
# else:
#     middleidx = palins.index(max(palins))
#     temp = max(palins)
#     print(str[middleidx-temp+1:middleidx+temp])
#
#
# # h, w = map(int, input().split())
# # n = int(input())
# # arr = [[0 for col in range(w)] for row in range(h)]
# #
# # for i in range(n):
# #     l, d, x, y = map(int, input().split())
# #     if d == 0:
# #         for j in range(l):
# #             arr[x - 1][y - 1 + j] = 1
# #     else:
# #         for k in range(l):
# #             arr[x - 1 + k][y - 1] = 1
# #
# # for row in range(h):
# #     for col in range(w):
# #         print(arr[row][col], end=" ")
# #     print()
# #
# # # w,h,b =map(int,input().split()) #def
# #
# # # n = int(input())  #개수를 입력받아 n에 정수로 저장
# # # d = [[0 for col in range(19)] for row in range(19)]
# # #
# # #
# # # for i in range(n):
# # #   x,y = map(int,input().split())
# # #   d[int(x-1)][int(y-1)]=1
# # #
# # #
# # #
# # # # for i in range(n):
# # #
# # #
# # #
# # # for i in range(19):
# # #   for j in range(19):
# # #     print(d[i][j],end=" ")
# # #   print()
# # #
# #
# #
# # #
# # # d=[]        #d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
# # # for i in range(24):  #[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
# # #  d.append(0)#각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.
# # #
# # # for i in range(n):
# # # d[a[i]] += 1
# # # temp=a[0]
# # # for i in range(1,n):
# # # if temp<a[i]:
# # # temp=temp
# # # else:
# # # temp=a[i]
# # #
# # # print(temp)
# # #
# # #
# # #
# # ## d = [list(map(int, input().split())) for _ in range(19)]
# # # n = int(input())
# # #
# # # for _ in range(n):
# # #     x, y = map(int,input().split())
# # #     for j in range(19):
# # #         if d[j][int(y-1)] == 0:
# # #             d[j][int(y-1)] = 1
# # #         else:
# # #             d[j][int(y-1)] = 0
# # #
# # #         if d[int(x-1)][j] == 0:
# # #             d[int(x-1)][j] = 1
# # #         else:
# # #             d[int(x-1)][j] = 0
#
# from collections import deque
# import math
# import sys
#
# sys.setrecursionlimit(100000)
#
#
# # 문자열을 1개씩 나눠서 리스트에 넣고,
# # 리스트 원소끼리 비교해서 같다면 다음것까지 비교하면서 cnt++해준다.
# # 만약 다를경우 cnt+문자열을 pop하고 temp에 넣는다. 다시 반복하다가 끝까지 확인하고, join하여
# # answer list에 append시키고, 상황을 n//2개씩까지 간후에, 가장짧은 길이의 리스트 원소를 출력해준다.
# # abcdddd>a,b,c,d,d,d,d > abc4d
# # ab, cd, dd, dd, d > abcd2ddd
#
#
# def solution(s):
#     if len(s) == 1:
#         return 1
#     def slicing(q, cnt, temp):
#         if len(q) <= 1:  # 종료조건
#             if cnt > 1:  # 마지막에 연속된 문자가 있을경우 예외처리
#                 head = str(cnt)
#                 temp += head + q[0]
#             else:
#                 temp += q[0]
#             print(temp)
#             return len(temp)
#         # [sss] ,cnt=2  > 3s > s
#         if q[0] == q[1]:  # 처음원소와 다음원소가 같다면.
#             cnt += 1
#         else:
#             if cnt > 1:
#                 head = str(cnt)
#                 temp += head + q[0]
#                 cnt = 1  # 빼줄때 초기화시킨다.
#             else:
#                 temp += q[0]
#         q.popleft()
#         return slicing(q, cnt, temp)
#
#     # 리스트 쪼개기
#     def uniting(s):
#         temp = list(s) #asdf > a,s,d,f
#         answer = []
#         result = []
#         for unit in range(1, len(s) // 2 + 1):  # 몇개씩 나눌건지 => 최대 len//2 개씩 나눌수있다.
#             print('문자열길이', len(s))
#             print('unit', unit)
#             print('횟수', math.ceil(len(s) / unit))
#             temp2 = []
#             for i in range(math.ceil(len(s) / unit)):  # 몇번 넣을건지
#                 start = unit * i
#                 end = start + unit
#                 if end > len(s):
#                     val = ''.join(temp[start:len(s)])
#                 else:
#                     val = ''.join(temp[start:end])
#                 temp2.append(val)
#                 print('temp2', temp2)
#                 print("*" * 25)
#             answer.append(temp2)
#             print("*" * 25)
#             print('answer', answer)
#         for i in answer:
#             q = deque(i)
#             x = slicing(q, 1, '')
#             result.append(x)
#         # print('result: ', result)
#         if not result:
#             return 0
#         else:
#             answer = min(result)
#         return answer
#     return uniting(s)
#
#
# s = 'aabbsdsasd'
# print(solution(s))
