# https://www.acmicpc.net/problem/2110

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def binary_search(axis,distance,c):
    count=1
    prev_axis=axis[0]

    for i in range(1,len(axis)):
        if axis[i]-prev_axis>=distance:
            count+=1
            prev_axis=axis[i]
            if count>=c:
                return True
    return False

if __name__ == "__main__":
    n, c = map(int, input().split())
    # 공백으로 리스트 입력
    axis=[]
    for _ in range(n):
        axis.append(int(input()))
    # 공유기를 설치하고, 인접한 공유기의 거리중에 작은 값을 구한다.
    # 가장 작은 값들을 모은것 중에 최대값을 출력한다.
    # 이분탐색으로 어떻게? > 일단 거리를 공유기로 나누고 최소 그 거리만큼일때를 기준으로 둔다?
    # 거리만큼이 안두어지면 이분탐색을 활용함. 좌표를 지정해 놓고 하는게 좀 어려움
    # 여유가 있을경우 > 남은 거리//공유기의 개수를 term ++ 로 해주면됨 >> 인데 좌표로 지정되어있으니 이게 문제
    # 여유가 없을경우 > 전부 -1 씩 해서
    # 다음좌표가 <= + term 인 곳으로잡고 잡고 잡아서 거리가 가장 짧은곳을 점검?
    # 이렇게 하지말고 그냥 생으로 이분탐색으로 일단 풀자

    # 1. 임의의 거리 distance를 지정
    # 2. axis를 순회하며 next-cursor가 distance보다 클경우, 중계기를 소모함.
    # 3. 끝까지 갔을때, 중계기를 모두 소모했다면 값을 저장하고, 값을 키워봄 // 중계기를 모두 소모하지 못했다면 값을 줄임
    axis.sort()
    start=0
    end=axis[-1]-axis[0]
    max_distance=0
    while start<=end:
        mid=(start+end)//2
        if binary_search(axis,mid,c):
            start=mid+1
            max_distance=max(mid,max_distance)
        else:
            end=mid-1
    print(max_distance)