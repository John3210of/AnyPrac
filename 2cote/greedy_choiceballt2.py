n, m = map(int, input().split())
lst = list(map(int, input().split()))
cnt = 0
for i in range(len(lst) - 1):
    for j in range(i+1, len(lst)):
        if lst[i] != lst[j]:
            cnt += 1

print(cnt)






















# # 볼링공 개수, 공의 최대 무게
# n, m = map(int, input().split())
# data = list(map(int, input().split()))
#
# # 1부터 10까지의 무게를 담을 수 있는 리스트
# weights = [0] * 11
#
# for x in data:
#     # 각 무게에 해당하는 볼링공의 개수 카운트
#     weights[x] += 1
#
# count = 0
# # 1부터 m까지의 각 무게에 대하여 처리
# for i in range(1, m + 1):
#     print('step', i, 'A가 무게가', i, '인 공을 선택')
#     print('A가 선택할 수 있는 경우의 수 = 무게가', i, '인 볼링공의 개수 = weights[i] =', weights[i])
#     n -= weights[i]  # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
#     print('B가 선택할 수 있는 경우의 수 = 남은 볼링공 중 무게가 i가 아닌 볼링공의 개수 = n - weights[i] = ', n)
#     count += weights[i] * n  # B가 선택하는 경우의 수와 곱하기
#     print('step', i, '수행결과 : A가 선택할 수 있는 경우의 수 * B가 선택할 수 있는 경우의수 = ', weights[i] * n)
#     print('현재까지 가능한 총 경우의 수 = ', count, '\n')
#
# print(count)