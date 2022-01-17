# 말이 이해가 되는지?
# 작성한 코드를 손에 익숙하게 해봐라

# LIFO = STACK // FIFO = QUEUE
# 먼저 먹은 접시가 가장 아래에 있는 개념 = STACK
# 줄을 서는 개념 = QUEUE // DEQUE를 사용하여 QUEUE의 속도를 빠르게 하여 사용 한다.
from chap9.structures import Node,Stack


def test_node():
    assert Node(1, None).item == 1  # assert = 주장한다// node(myval,nextadd)


def test_stack():  # stack은 3가지 기능이 요구된다.

    stack = Stack()  # push,pop,is_empty

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.pop() is None
    assert stack.isempty()


test_node()
test_stack()
