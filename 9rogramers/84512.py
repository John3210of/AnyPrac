# https://school.programmers.co.kr/learn/courses/30/lessons/84512 모음사전

# a =1 , aaaaa=5 순열? aa=2 aaa=3
# aaaae=6 i=1563
# 11112
# aaae=10
# 1117
from itertools import product
def solution(word):
    vowels = ["A", "E", "I", "O", "U"]
    words = []
    for i in range(1, 6):
        print(words)
        for j in product(vowels, repeat=i):
            words.append("".join(j))
    words.sort()
    return words.index(word) + 1
