# https://school.programmers.co.kr/learn/courses/30/lessons/43165 타겟넘버
import sys
sys.setrecursionlimit(100000)

def dfs_get_sum(numbers, count, target, cursor=0, temp_sum=0):
    if cursor == len(numbers):
        return count+1 if temp_sum==target else count
    
    positive=dfs_get_sum(numbers, count, target, cursor+1, temp_sum+numbers[cursor])
    negative=dfs_get_sum(numbers, count, target, cursor+1, temp_sum-numbers[cursor])
    return positive+negative

def solution(numbers, target):
    # 종료조건 numbers를 다 돌았을때
    # count는 덧셈이 끝났을경우에 target과 같다면 증가하여 리턴
    # 현재 수가 양수일 경우를 가정하여 계산한다.
    # 현재 수가 음수일 경우를 가정하여 계산한다.
    count = 0
    count = dfs_get_sum(numbers,count,target)
    return count