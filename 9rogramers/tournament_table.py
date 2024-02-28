# https://school.programmers.co.kr/learn/courses/30/lessons/12985
# 반 나누고 그안에 존재하지 않으면 비트길이의 로그값 만큼
# 반 나누고 그안에 둘다 존재하면 +1하고 다시 반나누기
# 8=2^3 >>3
# 4=2^2 >>2
# import math
# n,a,b=8,4,7
# answer=0
# lst=[i for i in range(1,n+1)]
# while True:
#     if abs(a - b) == 1 and (a // 2 != b // 2):
#         answer=1
#         break
#     lst_left = lst[:len(lst)//2]
#     lst_right = lst[len(lst)//2:]
#     if a in lst_left and b in lst_left: #한번더 해야할때
#         answer+=1
#         lst=lst_left
#     elif a in lst_right and b in lst_right: #한번더 해야할때2
#         answer+=1
#         lst=lst_right
#     else:
#         num=len(lst_left)*2
#         break
# answer += int(math.log(num, 2))
# print(answer)

def solution(n, a, b):
    answer = 0
    while a != b:
        answer += 1
        a = (a + 1) // 2
        b = (b + 1) // 2
    return answer
