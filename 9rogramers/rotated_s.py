# https://school.programmers.co.kr/learn/courses/30/lessons/76502 괄호 회전하기
def is_valid(s):
    stack = []
    brackets = {'(': ')', '[': ']', '{': '}'}
    for char in s:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False
    return len(stack) == 0

def solution(s):
    count = 0
    length = len(s)
    for i in range(length):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            count += 1
    return count
s="[](){}"
print(solution(s))

times=6
goal=15

for tri in range(1,times+1):
    print(2*(tri)+3*(6-tri))