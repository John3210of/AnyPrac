# https://www.acmicpc.net/problem/17266
import sys
input = sys.stdin.readline
import math
if __name__ == "__main__":
    # 설치할 수 있는 가로등에서 좌우로 이동하여 범위를 모두 충족할 수 있는지
    # 가로등의 높이는 적당히 큰수 (전체 길이) 에서 이분탐색으로
    # 0번째 위치에서 펼쳤을때 0이하, m번째 위치에서 펼쳤을때 n이상 + location[i]-location[i-1] <= height를 만족하도록
    n = int(input())
    m = int(input())
    location=list(map(int, input().split()))
    min_width=float('-inf')
    height=n
    if m == 1:
        height = n-location[0] if n-location[0] >= n/2 else location[0]
    else:
        for i in range(len(location)-1):
            min_width = max(math.ceil((location[i+1]-location[i])/2),min_width)
        start=0
        end=n
        while start<=end:
            mid=(start+end)//2
            if location[0]-mid <=0 and location[-1]+mid >= n and mid >= min_width: # 충분히 크다면
                height=mid
                end=mid-1
            else:
                start=mid+1
    print(height)

    '''
    문제의 핵심 : 구간이 존재한다면 (location[0]>1), 각 구간중에 최댓값을 구하는것
    min_width를 정하는 것이 이 문제의 핵심
    '''
