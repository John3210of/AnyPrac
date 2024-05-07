# https://www.acmicpc.net/problem/2775
import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lst=[]
    for _ in range(n):
        i=int(input())
        j=int(input())
        lst.append([i,j])

    dp=[[0]*15 for _ in range(15)]
    dp[0]=list(range(0,15))
    for i in range(1,15): # 층, 호수
        for j in range(1,15):
            dp[i][j] = sum(dp[i-1][:j+1])
    
    for row,col in lst:
        print(dp[row][col])