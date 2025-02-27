import sys
k, p, n = map(int,input().split())

# dp?
# k : 초기 바이러스 , p = 증가율, n = 지속시간
answer = (k*pow(p,n,1000000007))%1000000007
# answer = k * (p**n) % 100000007
print(answer)
# 걍 모듈러