from collections import deque

n = input()
lst = []
for i in n:
    lst.append(i)
lst2 = list(map(int, lst))
q = deque(lst2)
res = q.popleft()
while q:
    temp = q.popleft()
    if res == 0:
        res += temp
    elif temp == 0 or temp == 1:
        res += temp
    else:
        res *= temp

print(res)
