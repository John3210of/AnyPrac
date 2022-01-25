# 9-21 중복문자 제거
# 문자열 s가 주어지면 모든 문자가 한 번만 나타나도록 중복 문자를 제거합니다. 결과가 가능한 모든 결과 중에서 사전순으로 가장 작은지 확인해야 합니다.
# 제약: 1 <= 길이 <= 104 s는 영문 소문자로 구성됩니다.
# Q. 중복된 문자를 제거하기 // 사전식 순서로 나열하기

from collections import Counter
import math
import time


def del_dup(s):
    stack = []
    flag = 0

    # 1) 알파벳 갯수를 카운트 한다.
    cnter = Counter(s)

    for char in s:  ##   1342 cbac dcbc 3213 4323// c:4 b:2 a: 1 d: 1
        cnter[char] -= 1
        if cnter[char] == 0 and char not in stack:
            #  단 한개뿐이라면 건너뛰기 불가능
            stack.append(char)
            flag = 1

        if flag == 1 and char > stack[-1] and char not in stack:
            stack.append(char)

    print(stack)


if __name__ == "__main__":
    del_dup('cbacdcbc')
    del_dup('cccaaadddbbbccca')  # edgd case인데 set으로 정렬하여 문자의 존재 파악하고
    # count가 1이상이어도 가장 작은 문자일 경우에는 stack에 집어넣어주는 기능을 추가하면 될듯
    # adddbbbccca

    start = time.time()
    math.factorial(100000)
    end = time.time()
    print(f"{end - start:.5f} sec")
