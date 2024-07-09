import heapq

class MedianFinder:
    # 클래스구현, findMedian
    # 수가 매우 크므로 항상 리스트를 정렬하는 방법은 안됨
    # 리스트가 홀수개면 정렬된 리스트의 중간값
    # 짝수개면 중간 2개의 평균값
    # 입력 받으면서 정렬되는 자료구조를 사용해야함
    # 힙 2개를 이용해서 숫자를 반씩 저장 python식 최대힙을 사용
    # 홀수라면 최대힙의 루트값이 중간값
    # 길이가 같다면(짝수) 각 힙에서의 루트값을 뽑아서 평균을 내면됨
    # 일단 힙에 넣고, 그후에 들어오는 값
    def __init__(self):
        self.small_half = []
        self.large_half = []
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small_half, -num)
        heapq.heappush(self.large_half, -heapq.heappop(self.small_half))
        if len(self.small_half) < len(self.large_half):
            heapq.heappush(self.small_half, -heapq.heappop(self.large_half))
    def findMedian(self) -> float:
        if len(self.small_half) > len(self.large_half):
            return -self.small_half[0]
        return (-self.small_half[0] + self.large_half[0]) / 2.0