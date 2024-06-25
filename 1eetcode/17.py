# class Solution:
#     def dfs(self, index, string, digits, num_pad, combinations):
#         if index == len(digits):
#             combinations.append(string)
#             return
#         for char in num_pad[digits[index]]:
#             self.dfs(index + 1, string + char, digits, num_pad, combinations)

#     def letterCombinations(self, digits: str) -> List[str]:
#         if not digits:
#             return []
#         num_pad = {
#             '2': ['a', 'b', 'c'],
#             '3': ['d', 'e', 'f'],
#             '4': ['g', 'h', 'i'],
#             '5': ['j', 'k', 'l'],
#             '6': ['m', 'n', 'o'],
#             '7': ['p', 'q', 'r', 's'],
#             '8': ['t', 'u', 'v'],
#             '9': ['w', 'x', 'y', 'z']
#         }
#         # 모든 조합을 구한다.순서는 상관없음 각 버튼을 1번씩만 선택하는 조합
#         # dfs?
#         combinations = []
#         self.dfs(0, "", digits, num_pad, combinations)
#         return combinations
from itertools import product

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        num_pad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        
        # 각 숫자에 해당하는 문자 리스트를 구한다.
        letters = [num_pad[digit] for digit in digits if digit in num_pad]
        # itertools.product를 사용하여 가능한 모든 문자 조합을 생성한다.
        combinations = [''.join(combo) for combo in product(*letters)]
        
        return combinations