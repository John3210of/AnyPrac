import sys
input = sys.stdin.readline


def solution():
    dp=[0 for _ in range(13)]
    dp[0]=0
    dp[1]=1
    dp[2]=2
    # dp[n]=dp[n-3]+3, dp[n-2]+2,dp[n-1]+1 // n>3
    dp[3]=4
    for i in range(4,13):
        dp[i]=dp[i-3]+dp[i-2]+dp[i-1]
    return dp

if __name__ == "__main__":
    n = int(input())
    lst=[]
    for _ in range(n):
        lst.append(int(input()))
    dp=solution()
    for i in lst:
        print(dp[i])