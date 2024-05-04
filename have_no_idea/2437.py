import sys
from itertools import combinations
input = sys.stdin.readline

# 와 이걸 어케 생각해서 풀어 수학문제인데
# 1번째 는 1이 와야함
# 2번째는 1,2가 와야함
# 3번째는 1~4가 와야함
# n번째 숫자는 n-1번째의 합이 S일때 S+1이하의 숫자가 와야함
# [1,2] >> 합이 3이고 1,2를 가지고 있음 >> 3번째 자리에는 1,2,(1~4) 의 숫자가 와야함
# 만약 1,2,5 가 될 경우  1,2,3,5가 되어 S+1을 표현할 수 없어진다.

n = int(input())
weights=list(map(int, input().split()))
weights.sort()
if weights[0] > 1:
    print(1)
else:
    s=0
    for w in weights:
        if w > s+1:
            break
        s+=w
    print(s+1)



# 메모리초과
if __name__ == "__main__":
    n = int(input())
    lst=list(map(int, input().split()))
    # lst=[3, 1, 6, 2, 7, 30, 1]
    # 무게를 1씩 올리면서 가능한지 확인?
    # 최대값은 리스트 전체의 합
    # 조합가능한 무게를 모두 구하면서 연속되지 않은 숫자 구하기? 
    # >> 1000개에 대해 1~n까지의 모든 조합을 구한다?
    # 1,2,...,n-1,n 각 리스트에 대해 연속하지 않는 구간을 구한다.
    # n개씩의 합을 set형태로 저장한 후에, 리스트로 형변환후 연속되지 않는 부분을 찾는다.
    # 완전탐색은 메모리 초과

    max_weight=sum(lst)+1
    visited=[False]*max_weight
    visited[0]=True
    for i in range(1,len(lst)+1):
        for comb in combinations(lst,i):
            visited[sum(comb)]=True

    for i in range(len(visited)):
        if visited[i]==False:
            print(i)
            break
    

    

