# 최대 최소의 값들이 필요하다면? 힙을 쓰게된다. 유용하다.

# 힙 = ? 큰값이 상위에, 작은값이 하위에 있다. 아니라면 힙이 아니다.
# 완전이진 트리이면서 부모가 항상 자식보다 커야한다. => 최대힙
#       ''        최소값이 최상위에 있다면 ==> 최소힙
#계산편의를 위해 인덱스를 1부터 사용한다. 0에는 null
# 힙에서의 추출은 루트를 빼내는것.

class BinaryMaxHeap:    #__xxx__ << magic method
    def __init__(self): #클래스가 시작될때 실행되는 명령문
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]

    def __len__(self):
        # len() 연산을 가능하게 하는 매직 메서드 덮어쓰기(Override).
        return len(self.items) - 1

    def _percolate_up(self):
        # percolate: 스며들다.
        cur = len(self)
        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
        parent = cur // 2

        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            parent = cur // 2

    def _percolate_down(self, cur):
        biggest = cur
        left = 2 * cur
        right = 2 * cur + 1

        if left <= len(self) and self.items[left] > self.items[biggest]:
            biggest = left

        if right <= len(self) and self.items[right] > self.items[biggest]:
            biggest = right

        if biggest != cur:
            self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
            self._percolate_down(biggest)

    def insert(self, k):
        self.items.append(k)
        self._percolate_up()

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)

        return root