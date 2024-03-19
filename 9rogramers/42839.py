# https://school.programmers.co.kr/learn/courses/30/lessons/42839?language=python3 소수찾기
from itertools import permutations

def is_prime(number): # 소수판별
    if number == 2:
        return True
    if number <= 1:
        return False
    if number%2 ==0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
def generate_permutations(s, length):
    return [int(''.join(permutation)) for permutation in permutations(s, length)]

def solution(numbers):
    n = len(numbers)
    all_permutations = []
    answer=0
    for length in range(1, n + 1):
        all_permutations.extend(generate_permutations(numbers, length))
    for i in set(all_permutations):
        if is_prime(i):
            answer+=1
    return answer
