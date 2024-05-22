# https://www.acmicpc.net/problem/2075

import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    # 메모리 초과?
    # heap이 너무 많은 것들을 가지고 있지 않도록 해야함
    # 항상 n개까지만 가지고 있게 한다?
    # n번째로 큰수는 최대값으로부터 n번째까지의수
    # 가지고 있어야할 것은 가장 큰값부터 n개씩
    # 최소힙 기준으로 길이가 n이 되었을 경우에 heap_top과 input을 비교하여 input이 더 크다면 교체한다.
    n = int(input())
    graph=[]
    heapq.heapify(graph)
    for _ in range(n):
        lst = list(map(int,input().split()))
        for i in lst:
            if len(graph) < n:
                heapq.heappush(graph,i)
            else:
                if i>graph[0]:
                    heapq.heapreplace(graph,i)
    print(graph[0])

