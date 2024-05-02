# https://www.acmicpc.net/problem/2579
import sys
input = sys.stdin.readline
# 못푼 문제
# DP 문제의 접근방식
# f(0),f(1),f(2) 를 통해 f(3),…,f(n) 을 수식으로 풀어내는 식으로 한다.
def max_score(stairs):
    n = len(stairs)
    if n == 1:  # 계단이 한 개일 때는 해당 계단의 점수가 최대 점수
        return stairs[0]
    elif n == 2:  # 계단이 두 개일 때는 두 계단의 점수를 합한 값이 최대 점수
        return stairs[0] + stairs[1]

    # dp 배열 초기화
    dp = [0] * n
    dp[0] = stairs[0]  # 첫 번째 계단의 점수
    dp[1] = stairs[0] + stairs[1]  # 두 번째 계단까지의 최대 점수
    dp[2] = max(stairs[1] + stairs[2], stairs[0] + stairs[2])  # 세 번째 계단까지의 최대 점수

    # 동적 계획법을 사용하여 각 계단마다 최대 점수 계산
    for i in range(3, n):
        # 현재 위치에서 한 계단 올라온 경우와 두 계단 올라온 경우 중 최대값 선택
        # 이전에 연속된 세 개의 계단을 밟지 않도록 조건 추가
        dp[i] = max(stairs[i] + dp[i - 2], stairs[i] + stairs[i - 1] + dp[i - 3])

    return dp[-1]  # 마지막 계단까지의 최대 점수 반환

if __name__ == "__main__":
    n = int(input())  # 계단의 개수 입력
    stairs = [int(input()) for _ in range(n)]  # 각 계단의 점수 입력
    print(max_score(stairs))  # 최대 점수 출력

