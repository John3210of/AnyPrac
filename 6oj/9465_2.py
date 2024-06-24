import sys
input = sys.stdin.readline

def solution(dp,k):
    # 최초에 뗄수잇는것은 max(dp[0][0],dp[1][0])
    if k==1:
        return max(dp[0][0],dp[1][0])
    else:
        dp[0][1]+=dp[1][0]
        dp[1][1]+=dp[0][0]

        for i in range(2,k):
            dp[0][i]+=max(dp[1][i-1],dp[1][i-2])
            dp[1][i]+=max(dp[0][i-1],dp[0][i-2])

    return max(dp[0][k-1],dp[1][k-1])

if __name__ == "__main__":
    n = int(input())
    answer=[]
    for i in range(n):
        k=int(input())
        dp=[]
        for _ in range(2):
            dp.append(list(map(int,input().split())))
        answer.append(solution(dp,k))
    for ans in answer:
        print(ans)