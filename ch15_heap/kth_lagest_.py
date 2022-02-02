# 정수 배열 nums와 정수 k가 주어지면 배열에서 k번째로 큰 요소를 반환합니다.
# k번째 고유한 요소가 아니라 정렬된 순서에서 k번째로 큰 요소입니다.

# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
#
# k = 4
#
# def kth_largest(nums,k):
#     nums.sort()
#
#     print(nums[-k])
#     return
#
# kth_largest(nums,k)

############################################################

class BinaryMaxHeap:  # __xxx__ << magic method
    def __init__(self):  # 클래스가 시작될때 실행되는 명령문
        # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
        self.items = [None]
        print('__init__self.items: ',self.items)

    def __len__(self): ## 처음에 none을 넣었으니
        # len() 연산을 가능하게 하는 매직 메서드 덮어쓰기(Override).
        return len(self.items) - 1

    def _percolate_up(self):
        cur = len(self)
        print('percolate_up_cur: ',cur)

        # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
        parent = cur // 2
        print('percolate_up_parent: ', parent)
        while parent > 0:
            if self.items[cur] > self.items[parent]:
                self.items[cur], self.items[parent] = self.items[parent], self.items[cur]

            cur = parent
            print('in while, percolate_up_cur: ', cur)
            parent = cur // 2


    def insert(self, k):
        self.items.append(k)
        self._percolate_up()
        print('insert_k: ',k)
        print('dddd',self.items)


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

    def extract(self):
        if len(self) < 1:
            return None

        root = self.items[1]
        self.items[1] = self.items[-1]
        self.items.pop()
        self._percolate_down(1)
        print('빠질 root값:', root)
        return root


def test_maxheap_we_made(lst, k):
    maxheap = BinaryMaxHeap()

    for elem in lst:
        maxheap.insert(elem)
    print('maxdddddddddddddd',maxheap.items)

    answer = [maxheap.extract() for _ in range(k)][k - 1]

    print('answer: ', answer)
    return answer


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]

k = 4

test_maxheap_we_made(nums, k)
