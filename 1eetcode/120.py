class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # dp // left,right 나누어 정복
        # 계층마다 최소로 줄 수 있는 값을 택하여 저장한다. -> 최대 값을 넣어둘것
        if len(triangle)==1:
            return triangle[0][0]

        dp=[[float('inf') for _ in range(i)] for i in range(1,len(triangle)+1)]
        dp[0][0] = triangle[0][0]
        dp[1][0] = dp[0][0] + triangle[1][0]
        dp[1][1] = dp[0][0] + triangle[1][1]
        # parent에서 좌,우로 가고 값을 갱신한다.
        # 좌,우로 가는 곳이 겹칠 경우에 더 작은 값을 내려준다.
        # 최종값까지 간 후에, min(dp[-1])을 리턴한다.
        # 받을 곳 기준으로 생각한다.
        # 제일 앞,뒤가 아닌경우는 모두 부모 노드의 -1,0 중에 작은 값을 현재의 나와 더해준다.
        for i in range(2,len(triangle)):
            for j in range(len(triangle[i])):
                if j == 0:
                    dp[i][j] = triangle[i][j] + dp[i-1][j]
                elif j == len(triangle[i])-1:
                    dp[i][j] = triangle[i][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = triangle[i][j] + min(dp[i-1][j-1],dp[i-1][j])
        return min(dp[-1])