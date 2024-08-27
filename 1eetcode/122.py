class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 다음날 가격이 더 작으면 즉시 팔기
        # 시간복잡도 o(n), 공간복잡도 0(1)
        # 현재 주식가격과 내일 주식가격을 비교하기
        # 내일 주식 가격이 더 크다면 내일 팔고 temp를 갱신한다.
        # 내일 주식 가격이 더 작다면 temp만 갱신한다.
        # 인덱스에 대한 정보를 가지고 있어야 하나?
        profit = 0
        temp_price = prices[0]
        for i in range(len(prices)-1):
            if prices[i+1] > temp_price:
                profit += (prices[i+1] - temp_price)
            temp_price = prices[i+1]
        return profit