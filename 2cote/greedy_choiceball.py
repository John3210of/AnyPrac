# 걍 1,2,...,n 까지 조합 하는거 아닌가
# 볼링공

n, m = map(int, input().split())
weights = list(map(int, input().split()))
# value를 가진 경우의 수
lst = [0] * m
result = 0
for i in weights:
    lst[i - 1] += 1
print(lst)
for i in range(m):
    print('lst[i]: ',lst[i])
    n -= lst[i]  # a를 고르고
    print('n: ', n)
    result += lst[i] * n  # b를 골라
    print('after: ',result)

print(result)

#
# # sol1) n^2
# lst = []
#
# cnt = 0
# for i in range(n):
#     lst.append(weight[i])
#
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if lst[i] != lst[j]:
#             cnt += 1
# print(cnt)
