# https://school.programmers.co.kr/learn/courses/30/lessons/12946 하노이의 탑

# 재귀를 코딩하는 방법
# 1. 종료조건 선언
# 2. 비즈니스 로직의 정의를 선언

# 재귀는 일반적으로 for문으로 대체가 가능하고 for문일때 big(O)가 더 낮을 확률이 높음
# 하지만 코딩이라는건 유지보수의 용이성도 따져야하기 때문에 선언형인 재귀로 구현하는것이 더 간단하고 쉽다면 재귀를 선택할 수 있다.

# 한 번에 하나의 원판만 옮길 수 있습니다.
# 큰 원판이 작은 원판 위에 있어서는 안됩니다.
# 2번째 기둥에 n-1개의 원판을 옮기기 >> 보조판
# 3번째 기둥에 n번째 원판을 옮기기
# 3번째 기둥에 2번째 기둥에 있는 n-1개의 원판을 옮기기
def hanoi(n, start, end):
    answer = []
    hanoi_sub(n, start, end, 2, answer)
    return answer

def hanoi_sub(n, start, end, other, answer):
    if n == 1:
        answer.append((start, end))
    else:
        hanoi_sub(n - 1, start, other, end, answer)
        answer.append((start, end))
        hanoi_sub(n - 1, other, end, start, answer)
n = 3
print(hanoi(n, 1, 3))


# def hanoi(num_discs, source, target, auxiliary):
#     stack = [(num_discs, source, target, auxiliary)]
#     moves = []

#     while stack:
#         print(stack[0][1],stack[0][2])
#         discs, src, dest, aux = stack.pop()
#         if discs == 1:
#             moves.append((src, dest))
#         else:
#             stack.append((discs - 1, src, aux, dest))
#             stack.append((1, src, dest, aux))
#             stack.append((discs - 1, aux, dest, src))
#     return moves

# num_discs = 3
# source, target, auxiliary = 1, 3, 2
# print(hanoi(num_discs, source, target, auxiliary))


def hanoi(n,start,end):
    answer=[]
    hanoi_dfs(n,start,end,2,answer)
    return answer

def hanoi_dfs(n,start,end,sub,answer):
    if n==1:
        answer.append([start,end])
    else:
        hanoi_dfs(n-1,start,sub,end,answer)
        answer.append([start,end])
        hanoi_dfs(n-1,sub,end,start,answer)

def solution(n):
    return hanoi(n,1,3)

print(solution(3))