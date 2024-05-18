# https://www.acmicpc.net/problem/1966

from collections import deque
import sys
input = sys.stdin.readline

def solution(lst:list,priority:deque):
    # lst[0]=>총 문서의 개수, lst[1]=>priority[lst[1]]=> 가 몇번째로 인쇄되는지? >> 우선순위가 몇번째인지
    # 처음 priority의 index정보가 필요함
    if len(priority)==1:
        return 1
    priority_idx=deque([i for i in range(len(priority))])
    answer=[]
    while priority:
        value=priority.popleft()
        idx=priority_idx.popleft()
        if not priority or value >= max(priority):  # 다뺐을때는 요렇게 해야함
            answer.append(idx)
            if lst[1]==idx:
                return len(answer)
        else:
            priority.append(value)
            priority_idx.append(idx)
    return len(priority)

if __name__ == "__main__":
    n = int(input())
    lst=[]
    priority=[]
    for _ in range(n):
        lst.append(list(map(int,input().split())))
        priority.append(deque(map(int,input().split())))
    
    for i in range(n):
        print(solution(lst[i],priority[i]))