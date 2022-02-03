import sys

input = sys.stdin.readline

n = int(input())

stages = list(map(int, input().split()))

print(stages)


#######이게더심함
from collections import Counter


def solution(N, stages):
    # for i in stages에서 i보다 큰 수라면 i클리어++
    # i와 같다면 i실패자++
    # i실패자/i클리어 = 실패율
    # result => 실패율의 내림차순 정렬
    # 딕셔너리 형태로 i=i실패율로 저장하던가
    # [실패율,i] 형태로 list를 만들던가 해줘야함.
    lst = []
    stages.sort()
    fail_cnt = {i:0 for i in range(1,N+2)}
    print(fail_cnt)
    fail_cnt2 = Counter(stages)
    fail_cnt.update(fail_cnt2)
    print(fail_cnt)
    for i in range(1, N + 1):  # 1~N까지 1
        total_cnt = 0  # n스테이지에 도전한 사람의수 = stage idx가 n이상인사람.
        # 현재 스테이지에 머물러있는사람수 = 실패한 사람수
        for j in range(len(stages)):  # 2,1,2,6,2,4,3,3 > 1,2,2,2,3,3,4,6
            if not i in stages:
                if stages[j] > i:
                    total_cnt = len(stages) - j
                    print("total_cnt: ",total_cnt,i)
                    break

            if stages[j] == i:  # 1 , 1
                total_cnt = len(stages) - j
                print('total_cnt: ', total_cnt, stages[j])
                break

        fail_rate = fail_cnt[i] / total_cnt
        lst.append([fail_rate, i])

    lst.sort(key=lambda x: -x[0])
    print(lst)
    answer = []
    for i in range(len(lst)):
        answer.append(lst[i][1])
    print(answer)
    return answer


# #########제출 런타임에러뜸
# def solution(N, stages):
#     lst = []  # stages = [2, 1, 2, 6, 2, 4, 3, 3]
#     stages.sort()  # stages = [1, 2, 2, 2, 3, 3, 4, 6]
#     for i in range(1, N + 1):
#         cur_cnt = 0
#         for j in stages:
#             if i <= j:
#                 break  # i = 셀 숫자 // j = stages의 val
#
#         total_cnt = len(stages) - j
#         fail_rate = cur_cnt / total_cnt
#         lst.append([fail_rate, i])
#
#     lst.sort(key=lambda x: -x[0])
#     answer = []
#     print('lst: ', lst)
#     for i in range(len(lst)):
#         answer.append(lst[i][1])
#     print(answer)
#     return answer
#
#
# # 런타임에러
#
# n = 5
#
# stages = [2, 1, 2, 6, 2, 4, 3, 3]
#
# solution(n, stages)
#
################### 이거로 풀음
# def solution(N, stages):
#     lst = []
#     for i in range(1, N + 1):
#         total_cnt = 0
#         cur_cnt = 0
#         for j in stages:
#             if i <= j:
#                 total_cnt += 1
#                 if i == j:
#                     cur_cnt += 1
#         if cur_cnt == 0:    #런타임 에러나와서 여기 추가함
#             fail_rate = 0
#         else:
#             fail_rate = cur_cnt / total_cnt
#         lst.append([fail_rate, i])
#
#     lst.sort(key=lambda x: -x[0])
#     answer = []
#     for i in range(len(lst)):
#         answer.append(lst[i][1])
#     return answer
#
#
# def solution(N, stages):
#
#     lst = []
#     for i in range(1,N+1):  # stage 수
#         total_cnt = 0
#         cur_cnt = 0
#         for j in stages:    #user 수 돌고
#             if i <= j:          #1
#                 total_cnt += 1  #[2, 1, 2, 6, 2, 4, 3, 3]
#                 if i == j:
#                     cur_cnt += 1
#         fail_rate = cur_cnt / total_cnt
#         lst.append([fail_rate, i])
#     print(lst)
#     lst.sort(key= lambda x:-x[0])
#     print('sorted: ',lst)
#     answer=[]
#     for i in range(len(lst)):
#         answer.append(lst[i][1])
#     return answer
# lst=[2, 1, 2, 6, 2, 4, 3, 3]
# solution(5,lst)