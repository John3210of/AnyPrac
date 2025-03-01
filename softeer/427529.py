import sys,math

'''
0 - 2*2
1 - 3*3
2 - 5*5
3 - 9*9
4 - 17*17
..
(이전 행의 개수 + 이전 행의 개수 -1)**2
dp
'''
n = int(input())
dp = [0 for _ in range(16)]
dp[0]=4
dp[1]=9
dp[2]=25
for i in range(3,16):
    dp[i] = (int(math.sqrt(dp[i-1]))*2-1)**2
print(dp[n])



