import sys

# 난로와 반지름의 길이가 주어진다.
n = int(input())
half_radius = list(map(int,input().split()))

# 최대 공약수의 집합의 길이가 가장 큰 것을 반환하면 된다.
# n <= 100이므로 걍 다 세도 된다. 걍 greedy로 풀자

half_radius.sort()
answer = 1
for i in range(2,max(half_radius)+1):
    max_houses = 0
    for j in range(len(half_radius)):
        if half_radius[j] % i == 0:
            max_houses += 1
    answer = max(answer, max_houses)
print(answer)