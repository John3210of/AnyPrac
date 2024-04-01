# 1. 같은 숫자는 싫어
def solution(arr):
    # arr를 거꾸로 순회하여 stack을 확인하면서 넣어준다.
    # 마지막에 stack을 거꾸로 뒤집어서 반환한다.
    stack=[]
    while arr:
        if not stack or stack[-1] != arr[-1]:
            stack.append(arr.pop())
        else:
            arr.pop()
    return stack[::-1]

# 2.기능 개발
from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    days = deque()
    # 각 기능이 배포되기까지 걸리는 일수 계산하여 days 큐에 저장
    # 첫 번째 기능부터 순서대로 확인하며 배포 처리
    # 기능들 중 배포 가능한 것 확인
    for i in range(len(progresses)):
        remain = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(remain)
    while days:
        count = 1
        first = days.popleft()
        while days and days[0] <= first:
            days.popleft()
            count += 1
        answer.append(count)

    return answer

# 3. 올바른 괄호
def solution(s):
    if s[0] != '(' or s[-1] != ')':
        return False
    # 스택에 넣으면서 쌍을 이룰 수 있는지 확인
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack
