# https://school.programmers.co.kr/learn/courses/30/lessons/154539?language=python3 뒤에있는큰수찾기

def solution(numbers):
    result = [-1] * len(numbers)
    stack = []  # 현재 숫자보다 큰 수의 인덱스를 저장할 스택
    
    for i in range(len(numbers)):
        # 스택이 존재하고 스택의 인덱스에 있는 numbers의 숫자가 현재 숫자보다 작으면 stack에서 뽑아내고 그 인덱스를 가지는 number의 수를 저장
        while stack and numbers[stack[-1]] < numbers[i]:
            idx = stack.pop()
            result[idx] = numbers[i]
        # 스택에 현재 인덱스를 저장
        stack.append(i)
    
    return result


numbers=[2, 3, 3, 5]

print(solution(numbers))