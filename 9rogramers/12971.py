def solution(sticker):
    '''
    dp 같은데 0번째,1번째
    뽑는경우 안뽑는경우를 나눠서 가야할듯
    '''
    if len(sticker) <= 3:
        return max(sticker)
    dp = [0]*len(sticker)
    dp[0] = sticker[0]
    dp[1] = sticker[1]
    dp[2] = dp[0]+sticker[2]
    for i in range(3,len(sticker)-1):
        dp[i] = max(dp[i-2],dp[i-3]) + sticker[i]
    answer = max(dp)
    dp = [0]*len(sticker)
    dp[0] = 0
    dp[1] = sticker[1]
    dp[2] = sticker[2]
    dp[3] = sticker[1]+sticker[3]
    for i in range(4,len(sticker)):
        dp[i] = max(dp[i-2],dp[i-3]) + sticker[i]
    return max(answer,max(dp))

