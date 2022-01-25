# in queue
# push 1 2 3 4
# pop1 , 2
# push 2
from collections import deque


def get_card(num):
    # 1. 제일 위의 카드를 버린다.
    queue = deque([n for n in range(1, num + 1)])  # range범위내의 n을 리스트에 넣어줘
    while len(queue) > 1:
        queue.popleft()
        queue.append(queue.popleft())

    return queue.popleft()

    # queue = Queue([1,2,3,4,...N])
    # while len(queue) > 1:
    #     queue.pop()
    #     queue.push(queue.pop())


assert get_card(6) == 4
