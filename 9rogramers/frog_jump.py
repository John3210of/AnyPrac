# https://school.programmers.co.kr/learn/courses/30/lessons/12914 멀리뛰기
# 1과 2로 n을 만들수 있는 경우의수 >> 각 경우의 수의 조합
# 한 번 가는데, 1칸 또는 2칸을 점프할 수 있다고 하면,
# 현재 n칸째의 경우의 수를 구해본다고하면, n-1칸에서 1칸 뛰어서 온경우, n-2칸에서 2칸 뛰어서 온 경우
def count_ways_to_make_n(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    ways = [0] * (n + 1)
    ways[0] = 1 
    ways[1] = 1 

    for i in range(2, n + 1):
        ways[i] = ways[i - 1] + ways[i - 2]
    return ways[n]

n = 4
print(count_ways_to_make_n(n))
