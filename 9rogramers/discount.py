# https://school.programmers.co.kr/learn/courses/30/lessons/131127 할인행사
from collections import Counter
def solution(want, number, discount):
    want_dic=dict(zip(want, number))
    answer=0
    #원소의갯수-9번
    for i in range(len(discount)-9):
        ten_days_dic = Counter(discount[i:10+i])
        if ten_days_dic == want_dic:
            answer+=1
    return answer

want=["banana", "apple", "rice", "pork", "pot"]
number=[3, 2, 2, 2, 1]
discount=["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]

print(solution(want, number, discount)==3)