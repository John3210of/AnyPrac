# https://www.acmicpc.net/problem/7562
from collections import deque
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def solution(size,cursor,target):
    moving_rc = [(-2,-1),(-2,1),(-1,-2),(-1,2),(2,1),(2,-1),(1,-2),(1,2)]
    visited=[[0 for _ in range(size)] for _ in range(size)]
    queue=deque([(cursor[0],cursor[1],0)])
    visited[cursor[0]][cursor[1]]=1
    while queue:
        row,col,count=queue.popleft()
        if [row,col]==target:
            return count
        for drow,dcol in moving_rc:
            next_row=row+drow
            next_col=col+dcol
            if 0<=next_row<size and 0<=next_col<size and visited[next_row][next_col] != 1:
                visited[next_row][next_col]=1
                queue.append((next_row,next_col,count+1))
    return -1

if __name__ == "__main__":
    n = int(input())
    input_list=[]
    for _ in range(n):
        size=int(input())
        cursor=list(map(int,input().split()))
        target=list(map(int,input().split()))
        input_list.append([size,cursor,target])
    
    for size,cursor,target in input_list:
        print(solution(size,cursor,target))