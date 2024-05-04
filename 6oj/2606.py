# https://www.acmicpc.net/problem/2606
import sys
from collections import deque

input = sys.stdin.readline

def solution(dic:dict,m:int):
    # queue에서 원소를 꺼내고, 꺼낸 key의 value에 해당하는 모든 값들을 queue에 넣고, 
    # visited update를 하고 sum(visited) 가 answer
    visited=[0]*(m+1)
    visited[1]=1
    queue=deque([1])
    while queue:
        cursor = queue.popleft()
        for com in dic[cursor]:
            if visited[com] == 0:
                visited[com]=1
                queue.append(com)
    return sum(visited)-1


if __name__ == "__main__":
    # 1번 컴퓨터와 연결된 노드 bfs로 탐색하여 몇개인지 출력하기
    m=int(input())
    dic = {}
    for i in range(1,m+1):
        dic[i]=[]
    n = int(input())
    node=[]
    for _ in range(n):
        i,v = map(int,input().split())
        dic[i].append(v)
        dic[v].append(i)
    print(solution(dic,m))

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7


5
5
2 3
3 4
4 5
5 2
1 5

input:
9
8
2 3
4 5
6 7
8 9
2 5
4 7
6 9
1 8
output: 2
answer: 8

'''