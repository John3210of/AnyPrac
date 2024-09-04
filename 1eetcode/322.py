def coinChange(coins, amount):
    # DP 배열을 매우 큰 값으로 초기화 (이 경우 amount+1로 초기화)
    # 1원부터 amount 원까지를 만드는데 필요한 최소 동전수를 모두 구해놓는다.
    # 가능한 경우에 가지수가 더 작아지면 갱신시킨다.
    # 가능한경우란 coin 하나를 더할수있는경우. 그 경우는 dp[i-coin]에서 하나를 더 놓는 격임

    dp = [amount + 1] * (amount + 1)
    dp[0] = 0
    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)    # 여기서 min(dp[i])를 생각하는것이 어려웠음
    
    # 최종 결과 반환: dp[amount]가 초기값 그대로면 -1 반환, 아니면 dp[amount] 반환
    return dp[amount] if dp[amount] != amount + 1 else -1