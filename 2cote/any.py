from collections import deque


def slicing(q, cnt, temp):  # cnt 는 zip count이면서 cursor 역할까지.
    if len(q) == 1:
        temp += q[0]
        print(temp)
        print(len(temp))
        return len(temp)
    if q[0] == q[1]:  # 처음원소와 다음원소가 같다면.
        cnt += 1
    else:
        if cnt > 1:
            head = str(cnt)
            temp += head + q[0]
            cnt = 1  # 빼줄때 초기화시킨다.
        else:
            temp += q[0]

    q.popleft()
    return slicing(q, cnt, temp)


s = 'aaaacbbd'
a = list(s)
q = deque(a)

print(slicing(q, 1, 'test: '))
