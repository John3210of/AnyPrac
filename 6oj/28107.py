# https://www.acmicpc.net/problem/28107
import sys
input = sys.stdin.readline
from collections import deque


def keep_eating(sushi_list,i,eating_count,order):
    if not sushi_list:
        return
    while sushi_list:
        sushi=sushi_list.popleft()
        if sushi in order:
            eating_count[i]+=1
        else:
            sushi_list.appendleft(sushi)
            return
if __name__ == "__main__":
    # 인덱스가 우선순위를 가지고 겹치는 경우 둘다에서 제외시키고 몇개 사라졌는지 카운팅?
    # 뭔소린지 모르겠는데
    n,m = map(int,(input().split()))
    order_list=[]
    eating_count=[0 for _ in range(n)]
    for _ in range(n):
        order_list.append(list(map(int,input().split())))
    sushi_list=deque(map(int,input().split()))

    
    while sushi_list:
        sushi = sushi_list.popleft()
        for i in range(len(order_list)):
            if sushi in order_list[i]:
                eating_count[i]+=1
                keep_eating(sushi_list,i,eating_count,order_list[i])
            else:
                continue
            break
    print(eating_count)
