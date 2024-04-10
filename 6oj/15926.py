# https://www.acmicpc.net/problem/15926 현욱은 괄호왕이야

s = input()       # 괄호로만 구성된 문자열
valid = [0] * 1000  # 올바른 괄호 문자열 여부를 저장하는 배열
max_length = 0   # 최대 길이

stack = []  # 스택 초기화

# 올바른 괄호 문자열 여부 계산
for i in range(len(s)):
    if s[i] == '(':
        stack.append(i)
    else:
        if stack:
            valid[i] = valid[stack[-1]] = 1
            stack.pop()
# 최대 길이 계산
current_length = 0  # 현재 길이
for i in range(len(s)):
    if valid[i]:
        current_length += 1
        max_length = max(max_length, current_length)
    else:
        current_length = 0

print(max_length)
