# https://www.acmicpc.net/problem/11687
import sys
input = sys.stdin.readline
def find_right_zeros(n):
    zeros = 0
    while n >= 5:
        zeros += n // 5
        n //= 5
    return zeros

if __name__ == "__main__":
    # 10^m 할때 나머지가 0인 수중에 가장 작은수
    # 정수론 // x!의 오른쪽 0의개수 > 10을 인수로 얼마나 가지고 있는지
    # 10 = 2*5 >> 5의 배수를 가지는 갯수 
    # 2의 배수는 항상 5의배수보다 많으므로 5의 배수의 갯수만 세도 10의 배수는 같다고 볼 수 있다.
    # n! 의 0의 개수는 n을 5로 나눈 나머지와 같다?
    # N!의 5의 배수의 개수 ≡ N을 5로 나눈 몫
    # 이분탐색으로 푼다.
    
    m = int(input())
    start,end = 1,10*m
    flag=False
    while start < end:
        mid = (start+end)//2
        zeros=find_right_zeros(mid)

        if zeros < m:
            start = mid+1
        else:
            end = mid
        if m==zeros: flag=True
    if flag:
        print(end)
    else:
        print(-1)