import sys

input = sys.stdin.readline
from collections import deque

n = int(input())
m = []
for i in range(n):
    m.append(int(input()))
m.sort()
temp = 0
print(m)
q = deque(m)

while q:
    temp += q[0]+q[1]
    q.popleft()
    if q is None:
        break
    q.popleft()
    if q is None:
        break
    res = temp+q[0]
print(temp)
