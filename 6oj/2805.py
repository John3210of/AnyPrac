# https://www.acmicpc.net/problem/2805
import sys
input = sys.stdin.readline
if __name__ == "__main__":
    n, target = map(int, input().split())
    trees=list(map(int, input().split()))
    start=0
    end=max(trees)
    answer=2000000000
    # 최소 높이 = 나무의 최대값 - 필요 나무 길이 여기서 더 커져도됨 
    while start<=end: 
        height=0
        mid=(start+end)//2
        for tree in trees:
            if tree>=mid:
                height+=tree-mid
        if height>=target:
            start=mid+1
            answer=mid
        else:
            end=mid-1
    print(answer)