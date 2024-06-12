# https://www.acmicpc.net/problem/5430
import sys
import json
from collections import deque
input = sys.stdin.readline

def ac(operators,lst):
    queue=deque(lst)
    after_zip=deque([])
    reverse=False
    for i in range(len(operators)):
        if operators[i]=='R':
            if after_zip and after_zip[-1]=='R':
                after_zip.pop()
            else:
                after_zip.append('R')
        else:
            after_zip.append('D')
    while after_zip:
        oper = after_zip.popleft()
        if oper=='R':
            reverse = not reverse
        elif oper=='D':
            if not queue:
                print('error')
                return
            if reverse:
                queue.pop()
            else:
                queue.popleft()
    if reverse:
        queue.reverse()
    print("[" + ",".join(map(str, queue)) + "]")

if __name__ == "__main__":
    t = int(input())
    # 한줄에 여러개 입력받기
    lst=[]
    for _ in range(t):
        p = list(input().strip())
        n = int(input())
        t = json.loads(input())
        lst.append((p,t))
    for p,t in lst:
        ac(p,t)