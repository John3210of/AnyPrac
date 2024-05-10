
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp=[0]*(10**6+1)
    dp[1]=0
    for i in range(2,len(dp)):
        # 3으로 나누어떨어지는지, 2로 나누어떨어지는지, -1을 할건지
        dp[i]=dp[i-1]+1
        if i%3==0: dp[i]=min(dp[i//3]+1,dp[i])
        if i%2==0: dp[i]=min(dp[i//2]+1,dp[i])
    print(dp[n])
