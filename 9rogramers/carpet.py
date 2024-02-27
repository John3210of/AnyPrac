# https://school.programmers.co.kr/learn/courses/30/lessons/42842?language=python3
def solution(brown, yellow):
    total = brown + yellow
    for i in range(1, int(total**0.5) + 1):
        if total % i == 0:
            width = total // i
            height = i
            if (width - 2) * (height - 2) == yellow:
                return [width, height]