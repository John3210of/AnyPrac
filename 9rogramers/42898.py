def solution(m, n, puddles):
    '''
    최단 경로의 개수, 오른쪽 아래로만 이동이 가능
    경우의수를 모두 재는건 아닌거 같고
    [1, 1, 1, 1], 
    [1, 0, 1, 2], 
    [1, 1, 2, 4]
    '''
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for x,y in puddles:
        graph[y-1][x-1] = -1
        
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0][0] = 1
    
    for i in range(1,n):
        if graph[i-1][0] == 0 and dp[i-1][0] == 1:
            dp[i][0] = 1
        else:
            dp[i][0] = 0
    for i in range(1,m):
        if graph[0][i-1] == 0 and dp[0][i-1] == 1:
            dp[0][i] = 1
        else:
            dp[0][i] = 0

    for row in range(1,n):
        for col in range(1,m):
            up, left = graph[row-1][col], graph[row][col-1]
            if up + left == -2 or graph[row][col] == -1:
                continue
            elif up == -1:
                dp[row][col] = dp[row][col-1]
            elif left == -1:
                dp[row][col] = dp[row-1][col]
            else:
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
    return dp[-1][-1]%1000000007