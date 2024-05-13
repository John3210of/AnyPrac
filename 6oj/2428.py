# https://www.acmicpc.net/problem/2428
import sys
input = sys.stdin.readline

def binary_search(lst):
    # 크기가 비슷할때 검사해야함 
    # 검사가 필요없는곳과 필요한곳의 경계까지 가야함
    # 반환할 수는 검사해야할 파일의 개수
    start=0
    end=len(lst)-1
    answer=0
    while start <= end:
        mid=(start+end)//2
        if lst[0] >= lst[mid]*(0.9): #비슷비슷할때==>더 뒤로 물려서 비슷한지 봐야함
            answer = mid
            start = mid+1
        else: # 더 클때 > 더 앞으로 당겨야함
            end = mid-1
    return answer
if __name__ == "__main__":
    n = int(input())
    lst=sorted(list(map(int, input().split())))
    # 이분탐색으로 몇개가 나머지인지 구해서 더하면됨
    count=0
    for i in range(len(lst)):
        count += binary_search(lst[i:]) # 파이선 리스트 슬라이싱 복사 메커니즘?
    print(count)

import sys
input = sys.stdin.readline

def binary_search(lst, start, end,target):
    answer = 0
    while start <= end:
        mid = (start + end) // 2
        if lst[target] >= lst[mid] * 0.9:
            answer = mid - i
            start = mid + 1
        else:
            end = mid - 1
    return answer

if __name__ == "__main__":
    n = int(input())
    lst = sorted(list(map(int, input().split())))
    count = 0
    for i in range(len(lst)):
        count += binary_search(lst, i, len(lst) - 1,i)
    print(count)
# 리스트 슬라이싱으로 복사는 앵간하면 피하는게 좋을듯 