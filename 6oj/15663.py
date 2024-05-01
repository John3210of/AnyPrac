# https://www.acmicpc.net/problem/15663
# 백트래킹(dfs)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
nums = list(map(int, input().split()))
visited = [False] * n
nums.sort()
result = []
def backtracking(k):
    if k == m:
        print(*result)
        return
    remember = 0
    for i in range(n):
        if not visited[i] and remember != nums[i] :
            visited[i] = True
            result.append(nums[i])
            remember = nums[i]
            backtracking(k+1)
            visited[i] = False
            result.pop()
backtracking(0)

# 순열 라이브러리로 해결
from itertools import permutations
N, M = map(int, input().split())
numbers = list(map(int, input().split()))
# N, M=4,2
# numbers=[9,7,9,1]
for perm in sorted(set(permutations(numbers, M))):
    print(*perm)


# 초안
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
# 조합의 길이가 m이 될때까지 탐색한다.
# 1~8까지의 리스트를 가지고 리스트 전체를 순회하면서 1개씩 찾는다.
# 제자리부터 ~ 리스트의 끝까지를 탐색한다.
def dfs(index,m,numbers,temp):
    # 종료조건 : 할당 개수를 채웠거나, 남아있는 수의 개수가 추가 해야 할 개수보다 적으면 중지
    if len(temp)==m or sum(numbers)+len(temp)<m or numbers[index]<1:
        return
    # 해야할일 : 지금 위치를 temp에 더하고, 리스트의 끝까지 재귀 탐색시키기
    numbers[index]-=1
    print(numbers)
    temp.append(index)
    for i in range(len(numbers)):
        dfs(i,m,numbers[:],temp)

def solution(m,lst):
    numbers=[0]*(max(lst)+1)
    print(max(lst))
    answer=[]
    for i in lst:
        numbers[i]+=1
    for i in range(len(numbers)):
        if numbers[i]!=0:
            temp=[]
            dfs(i,m,numbers[:],temp)
            answer.append(temp)
    return answer

# if __name__ == "__main__":
    # n,m = map(int, input().split())
    # lst=list(map(int, input().split()))
    # print(n,m)
    # print(lst)

    # n,m=4,2
    # lst=[9,7,9,1]
    # answer=solution(m,lst)
    # print(answer)
