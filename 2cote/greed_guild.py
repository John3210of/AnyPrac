from collections import deque

n = int(input())
lst = list(map(int, input().split()))
lst.sort()
q = deque(lst)
cnt = 0
# 2 3 1 2 2 >> 3 2 2 2 1
while q:
    for _ in range(q[0]):
        q.popleft()
        if len(q) == 0:
            break  # 함수로 만들어서 리턴하면더 깔끔할듯?
    if len(q) == 0:
        break
    cnt += 1
print(cnt)
