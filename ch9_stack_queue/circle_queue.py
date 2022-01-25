# circle size 설정하기
# Q_size = 5
# class circle_queue :
#     def __init__(self):
#         self.front = 0
#         self.rear = 0
#         self.items = [None] * Q_size
#
#     def isEmpty(self):  # isempty 구현하기
#         return self.front == self.rear
#
#     def isFull(self):
#         return self.front == (self.rear + 1) % Q_size
#
#     # push 구현하기
#
#     # pop 구현하기
#
#     # index % size로 rear, front pointer 이동시키기

Q_size = 6

class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * Q_size

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return self.front == (self.rear + 1) % Q_size

    def clear(self):
        self.front = self.rear

    def __len__(self):
        return (self.rear - self.front + Q_size) % Q_size

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % Q_size
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % Q_size
            return self.items[self.front]

    def peek(self):  # front 부분을 뽑아줌
        if not self.isEmpty():
            return self.items[(self.front+1) % Q_size]
        # == self.items[1]

    def print(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front + 1:self.rear + 1]
        else:
            out = self.items[self.front + 1:Q_size] + self.items[0:self.rear + 1]

        print("[f=%s, r=%d] ==> " %(self.front, self.rear), out)


if __name__ == "__main__":
    cirqueue = CircularQueue()

    cirqueue.enqueue(20)
    cirqueue.enqueue(30)
    cirqueue.enqueue(40)
    cirqueue.enqueue(40)
    cirqueue.enqueue(40)
    cirqueue.enqueue(40)

    print(cirqueue.peek())
    cirqueue.print()
