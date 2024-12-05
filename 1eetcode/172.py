class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 끝에붙은 0의개수 > 소인수분해하여 10의 개수 > 2*5가 몇개있는지
        # 5가 몇개 있는지를 센다면
        # 5로 나누어 떨어지는만큼? + 5의 n제곱
        if n < 5:
            return 0
        count = 0
        for i in range(5,n+1,5):
            while i%5 == 0:
                count += 1
                i = i/5
        return count