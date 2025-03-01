# from itertools import combinations
# n, k = map(int,input().split())
# things = []
# for _ in range(n):
#     w,v = map(int,input().split())
#     if w <= k:
#         things.append([w,v])
# '''
#     경우의수? dp? 물품의수가 100개 조합
#     일단 못넣는거 부터 다빼
#     가벼운거부터 넣고 꽉차면 탐색 그만
#     몇개를 집을지 알 수가 없음
#     1개를 집을때 가능한거 중에 최대 가격을 저장
#     2개를 집을때 가능한거 중에 최대 가격을 저장 > 1개를 집은 경우에서 다른걸 집어야하는데
#     k = 담을수 있는 최대 무게
#     w = 현재 무게
#     v = 현재 가격
# '''
# dp = [0 for _ in range(len(things))]
# max_val = 0
# for i in range(1,len(things)+1):
#     combs_list = combinations(things,i)
#     for combs in combs_list:
#         temp_value_sum = 0
#         temp_weight = 0
#         for comb in combs:
#             temp_value_sum += comb[1]
#             temp_weight += comb[0]
#         if temp_weight <= k:
#             max_val = max(max_val,temp_value_sum)
# print(max_val)


'''
이렇게 푸는게 아니라 저장할수 있는 무게에서 value를 가장 크게 가질 경우
4 7
6 13
4 8
3 6
5 12
'''
n, k = map(int,input().split())
things = []
for _ in range(n):
    w,v = map(int,input().split())
    if w <= k:
        things.append([w,v])
things.sort()
dp = [0 for _ in range(k+1)]
for w,v in things:
    for weight in range(k,w-1,-1):
        dp[weight] = max(dp[weight],dp[weight-w]+v)
print(max(dp))