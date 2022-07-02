# n = str(input())
#
# p = len(n) // 2
# front = 0
# back = 0
# for i in range(p):
#     front += int(n[i])
#     back += int(n[-i - 1])
#
# if front == back:
#     print("LUCKY")
# else:
#     print("READY")
# import math
# import time
#
# arr = [1, 2, 354, 1, 4, 62, 22, 4624, 263, 234, 324, 231, 2, 3, 5, 7, 8, 9, 4, 4, 23, 9886, 64]
# n = 9886 + 64
# start = time.time()
#
#
# def solution(arr, n):
#     # 투포인터로 더했을때 n이 나오면 return true
#     # 정렬 + 이분 탐색
#     left = 0
#     answer = 0
#
#     return answer
#
#
# print(solution(arr, n))
# math.factorial(100000)
# end = time.time()
# print(f"{end - start:.5f} sec")

n = 17


def solution2(n):
    # 이진수로 변환 > str으로 변환 > 1의 개수 세기
    # > n보다 작은 수 1의 개수 > n과 1의 개수가 같은 경우의 수 출력
    cnt = 0
    answer = 0
    ntoBin = format(n, 'b')
    nToList = list(ntoBin)
    temp = 0
    print(ntoBin)
    for x in ntoBin:
        print(x)
        temp += int(x)
    print('temp: ', temp)
    # for i in range(n):


    for x in nToList:
        if x == '1':
            cnt += 1
    for i in range(n):
        temp = 0
        op = format(i, 'b')
        opToList = list(str(op))
        for y in opToList:
            if y == '1':
                temp += 1
        if temp == cnt:
            answer += 1
    return answer


print(solution2(n))

phone_number = '01012345678'
phone_number2 = '010-1234-5678'
phone_number3 = '+82-10-1234-5678'


def solution(phone_number):
    # 유형 1의 경우 010으로 시작하며 -4자리-4자리 숫자 존재한다.
    # 유형 2의 경우 010으로 시작하며 8자리 숫자 존재한다.
    # 유형 3의 경우 +82-10-4자리-4자리 숫자 존재한다.

    answer = 1
    return answer
