from collections import deque

s1 = input()
result = []
s = '12312312312312'
cnt = 1
for length in range(1, len(s) // 2):
    lst = [s[i:i + length] for i in range(0, len(s), length)]
    print(lst)
    q = deque(lst)
    while len(q) > 1:
        if q[0] == q[1]:
            cnt += 1
            q.popleft()
        else:
            head = cnt
            if cnt == 1:
                result.append(q.popleft())
            else:
                result.append(str(head) + q.popleft())
            cnt = 1
        # print('result: ', result)


