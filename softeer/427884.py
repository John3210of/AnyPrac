import sys
k,p,n = map(int,input().split())

ten_pow = pow(p,10,1000000007)
answer = (k*pow(ten_pow,n,1000000007))%1000000007
print(answer)