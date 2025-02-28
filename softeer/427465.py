import sys
input = sys.stdin.readline
n = int(input())
heights = list(map(int,input().split()))

# dp? greedy?
'''
몇칸까지 갈수있는것도 없어. 최대 3000개라는점

한칸씩 이동하면서, 
이전칸에서 가장 크면서 나보다 작은 값에 + 1을 한다.
> 이게 제일 문제인데
1 5 2 3 4 6 8
1 1 1 1 1 1 1
1 2 1 1 1 1 1
1 2 2 1 1 1 1
1 2 2 3 1 1 1
# 3번째 인덱스로부터, 1칸씩 이동하며 이전의 가장 크면서 나보다 작은 값을 구해야 한다.
#이전 값들의 모음집(bound) 중에 높이가 나보다 작으면서 이동거리가 가장 큰값에 + 1
'''
distance = [1 for _ in range(n)]
if n == 1:
    print(1)
else:
    if heights[1] > heights[0]:
        distance[1] = 2
    for i in range(2,n):
        bound = distance[:i]
        for j in range(len(bound)):
            if heights[j] < heights[i]:
                distance[i] = max(bound[j] + 1,distance[i])
    print(max(distance))