# 최소힙이던 최대힙이던 시간복잡도는 같다.
class MaxHeap:  # class 부르기
    def __init__(self):  # parent 값에서 left right 때문에
        self.val = [None]  # 초기값 None으로 시작함.

    def __len__(self):  # 매직 메서드 덮어쓰기
        return len(self.val) - 1  # None값을 넣어주었으니, len계산때 1을 빼주는것

    def insert(self, k):  # heap에 leaf를 입력 하는 함수
        self.val.append(k)  # 변수k를 val 리스트에 append
        cursor = len(self)  # 가장 끝 요소에 커서 위치.
        parent = cursor // 2  # left 라면 2*cursor, right 라면 2*cursor + 1 이므로 # parent 는 항상 cursor // 2

        # 스왑하며 올라가는 로직
        while parent > 0:  # leaf부터 root까지 올라간다. level n >> n-1 >>... >> 0
            if self.val[cursor] > self.val[parent]:  # 만약 현재 커서(자식노드)가 가르키는 값이 부모보다 크다면
                self.val[cursor], self.val[parent] = self.val[parent], self.val[cursor]  # 스왑이 일어난다.
            cursor = parent  # level up
            parent = cursor // 2
        return self.val

    def extract(self):  # heap의 root를 추출하는 함수
        if len(self) < 1:  # val의 list에 값이 없을 경우
            return None
        self.val[1], self.val[-1] = self.val[-1], self.val[1]  # root와 leaf를 교체하여 pop하기
        pop_val = self.val.pop()  # 결과적으로 target이었던 root값이 pop됨
        # 다시 힙으로 만드는 과정
        root = 1  # 스왑된 값이 현재는 루트에 있음.
        cursor = root  # 커서를 루트에 놓음.

        while True:  # 스왑하며 내려가는 로직
            left = 2 * cursor  # 좌,우를 비교해서 들어갈 예정
            right = 2 * cursor + 1
            if right > len(self):  # 자식이 없거나 left에서 끝날경우 예외처리
                if left == len(self):
                    if self.val[cursor] <= self.val[left]:
                        self.val[cursor], self.val[left] = self.val[left], self.val[cursor]
                break
            if (self.val[cursor] < self.val[left]) and (self.val[cursor] >= self.val[right]):  # 좌로 내려갈래
                self.val[cursor], self.val[left] = self.val[left], self.val[cursor]
                cursor = left
            elif (self.val[cursor] >= self.val[left]) and (self.val[cursor] < self.val[right]):  # 우로 내려갈래
                self.val[cursor], self.val[right] = self.val[right], self.val[cursor]
                cursor = right
            else:
                break

        return pop_val


def Maxheapsort(lst):
    heap = MaxHeap()
    for i in lst:
        heap.insert(i)
    res = []
    for _ in range(len(lst)):
        res.append(heap.extract())
    res.sort(reverse=False)
    return res


lst = [3, 4, 1, 5, 5, 7,21,543,1212,2,3,55,100]
print(Maxheapsort(lst))
