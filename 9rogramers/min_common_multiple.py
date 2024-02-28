# https://school.programmers.co.kr/learn/courses/30/lessons/12953?language=python3

# import math
# math.gcd()
def gcd(a, b):
    """두 수의 최대공약수를 구하는 함수"""
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """두 수의 최소공배수를 구하는 함수"""
    return a * b // gcd(a, b)

arr=[2,6,8,14]

a_before=arr[0]
for a in arr[1:]:
    a_after=a
    a_before = lcm(a_before,a_after)
