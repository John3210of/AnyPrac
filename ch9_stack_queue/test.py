class MyCircularQueue:

    def __init__(self, k: int):
        # 원형 큐의 최대 갯수
        self.maxlength = k
        # 값이 들어있는 큐의 갯수    >>> node index 로 쓰이고 있음.
        self.items = [None] * k
        # 값이 들어있는 가장 앞의 큐 >>> 포인터가 가르키고 있는 index
        self.front = 0
        # 값이 들어있는 가장 뒤의 큐 >>> 포인터가 가르키고 있는 index
        self.rear = 0

    def isEmpty(self) -> bool:   # >>> 후에 쓰일 함수들은 먼저 선언 하는편이 좋음
        # 큐에 값이 하나도 없는지 확인하는 함수
        # if self.front == self.rear and self.queue[self.front] is None:
            return self.front == self.rear

    def isFull(self) -> bool:
        # 큐에 값이 꽉차있는지 확인하는 함수
        # if self.front == self.rear and self.queue[self.front] is not None:
            return self.front == (self.rear+1) % self.maxlength


    def enQueue(self, value: int) -> bool:
        # 큐를 추가하는 함수 >>> bool형태로 반환하기로 하였음.
        if self.isFull():
            # raise IndexError("Queue is full")
            # 큐에 값이 모두 들어있으면
            return False
        else:
            # 뒤쪽 포인터가 원형 큐에서 가리키는 곳의 한칸 뒤로 이동
            self.rear = (self.rear + 1) % self.maxlength
            # 그 값을 quueue의 value값으로 저장
            self.items[self.rear] = value
            # 성공하면 리턴!
            return True


    def deQueue(self) -> bool:
        # 큐를 제거하는 함수
        if self.isEmpty():
            # raise IndexError("Queue is Empty")
            # 큐에 값이 하나도 없으면
            return False
        else:
            # 큐에 값이 하나라도 있으면
            # 앞쪽 포인터가 원형 큐에서 가리키는 곳의 한칸 뒤로 이동
            self.front = (self.front + 1) % self.maxlength
            # 원래 값이 있던 큐의 값은 사라진다.
            self.items[self.front] = None
            # 성공하면 리턴!
            return True

    def Front(self) -> int:
        # 큐의 가장 앞쪽 값을 리턴하는 함수
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        return self.items[(self.front + 1) % self.maxlength] # >>> 이부분이 맞나?
                #self.queue
    def Rear(self) -> int:
        # 큐의 가장 뒤쪽 값을 리턴하는 함수
        if self.isEmpty():
            raise IndexError("Queue is Empty")
        return self.items[(self.rear + 1) % self.maxlength]


    # def print(self):
    #     out = []
    #     if self.front < self.rear:
    #         out = self.value[self.front + 1:self.rear + 1]
    #     else:
    #         out = self.value[self.front + 1:self.maxlength] + self.value[0:self.rear + 1]
    #
    #     print("[f=%s, r=%d] ==> " % (self.front, self.rear), out)


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

if __name__ == "__main__":

    cirqueue = MyCircularQueue(5)

    cirqueue.enQueue(20)
    cirqueue.enQueue(30)
    cirqueue.enQueue(40)

    # cirqueue.print()
