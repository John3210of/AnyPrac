# https://programmers.co.kr/learn/courses/30/lessons/42586
# 프로그래머스 스택/큐 기능개발 문제

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

# 조건1. 가장 왼쪽의 진행도가 100이 되면 pop한다.
#       >>만약 오른쪽의 진행도가 100이라면 계속해서 같이 pop한다.
# 조건2. pop한 index의 갯수를 세서 answer list에 넣어준다.
#       >>만약 answer index의 합과 len이 같아지면 결과값을 리턴한다.

i = 0
answer = []
day = 1

while sum(answer) != len(progresses):
    len_cnt = 0
    # total = progresses[i] + day * speeds[i]
    if progresses[i] + day * speeds[i] >= 100:  # 100이 넘어 pop해야 할 경우
        len_cnt += 1
        # 다음원소 같이 빼낼지 판단
        for j in range(i + 1, len(progresses)):  # 포인터 원소가 100이상일 경우, 같이 pop해줄수 있는원소가 몇개 있는지 찾는다.
            # total_r = progresses[j] + day * speeds[j]
            next_pointer = j
            if progresses[j] + day * speeds[j] >= 100:
                len_cnt += 1
            else:
                break
        answer.append(len_cnt)
        i = next_pointer
        day += 1
    else:
        day += 1

print(answer)


# 제출 코드

# def solution(progresses, speeds):
#     answer=[]
#     day=1
#     i=0
#     while sum(answer) != len(progresses):
#         len_cnt = 0
#         total = progresses[i] + day * speeds[i]
#         if total >= 100:
#             len_cnt += 1
#             for j in range(i + 1, len(progresses)):
#                 next_pointer=j
#                 total_r = progresses[j] + day * speeds[j]
#                 if total_r >= 100:
#                     len_cnt += 1
#                 else:
#                     break
#             answer.append(len_cnt)
#             i=next_pointer
#             day+=1
#
#         else:
#             day += 1
#
#     return answer
