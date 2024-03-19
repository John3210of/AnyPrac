# https://school.programmers.co.kr/learn/courses/30/lessons/12907 거스름돈

def solution(n, money):
    # dp로 접근
    # money의 동전을 순회하면서 coin으로 n원을 만드는법을 갱신시킨다.
    # dp[n] => 누적되며 더해지는 n원을 만드는 방법의 수
    # n원까지 가는거지만 n원을 만드는법은 예를들어 5원을 만드는 방법은 기존 5원까지 구했던 방법의수 + 5-coin 원을 만드는 방법의 수
    dp = [0] * (n+1)
    dp[0] = 1
    for m in money:
        for i in range(m, n+1):
            dp[i] = dp[i] + dp[i-m]
    return dp[n]%1000000007


print(solution(5, [1, 2, 5]) == 4)