# https://www.acmicpc.net/problem/2512
# 모든 인풋의 합 >= 전체 예산의 합 => 그대로 배정할수있으니 가장 큰 value를 return
# 아닐경우 상한액을 계산해야함. 우선 가장 작은 값을 기준으로 잡고 나머지를 계산. 
# 120 110 140 150
# 485(burget) > 길이로 나누어서 121을 우선 배정시킴
# 남는수가 발생할 경우 뺀 값 + 나머지값을 더함  11+1+1 > 13
# 임계점에서 남은 녀석들을 다시 공평하게 나눠줌 >> 마지막에 1이 남는경우 그냥 return
# dfs?
import sys
input = sys.stdin.readline
n=int(input())
lst=list(map(int, input().strip().split()))
burget=int(input())

lst.sort()
if burget >= sum(lst):
    print(max(lst))
else:
    val=burget//len(lst)
    remain=0
    answer=0
    while True:
        val=burget//len(lst)
        remain = burget - val*len(lst)
        for i in range(len(lst)):
            lst[i] -= val
            if lst[i] <= 0:
                remain -= lst[i]
                lst[i]=0
        for i in range(len(lst)):
            if lst[i]!=0:
                break
        answer+=val
        burget=remain
        lst=lst[i:]
        if lst[0]==0 or len(lst) > val:
            break
    print(answer)


# 접근이 잘못되었음.
# 이진 탐색으로 풀어야함

import sys

def find_max_budget(lst, budget):
    start = 0
    end = max(lst)
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total = 0

        for req in lst:
            total += min(req, mid)

        if total <= budget:
            result = mid
            start = mid + 1
        else:
            end = mid - 1

    return result

if __name__ == "__main__":
    input = sys.stdin.readline
    n = int(input())
    lst = list(map(int, input().split()))
    total_budget = int(input())

    answer = find_max_budget(lst, total_budget)
    print(answer)
