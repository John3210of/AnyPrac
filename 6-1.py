# Q1.유효한 팰린드롬인가?
# https://sooftware.io/regex/ 정규표현식
# https://ichi.pro/ko/paisseon-eseo-munjayeol-eseo-teugjeong-munjaleul-jegeohaneun-5gaji-daleun-bangbeob-194478292048569
# 문자열에서 특정문자 지우는 방법 블로그

import re   # 정규표현식

def isPalindrom(str):

    # 조건1) 대소문자 구별x >> 모든 문자를 소문자로 바꿔주기
    result = str.lower()

    # 조건2) 영문과 숫자만 받고 특수문자는 패스하기>> 정규 표현식 사용
    # [a-zA-Z0-9] : 모든 알파벳 문자 및 숫자
    # [^0-9] : ^가 맨 앞에 사용 되는 경우 해당 문자 패턴이 아닌 것과 매칭
    result = re.sub("[^a-z0-9]","", result)

    # 조건3) 팰린드롬 >> slicing
    if result == result[::-1]:
        isPalin = True
    else:
        isPalin = False

    print(isPalin)


if __name__ == "__main__":

    print('검증할 문장: ',end='')
    sentence=input()
    isPalindrom(sentence)




# # Q1.유효한 팰린드롬인가?
#
# def isPalindrom(str):  # 투포인터로 가는 방법도 있다.
#     ispalin = True
#
#     #excp) 대소문자 구별x
#     str = str.lower()   # 반환형이 있는 함수이다.
#     #excp) 영문과 숫자만 받기
#     if not str.isalnum():
#         return False
#
#     for i in range(len(str) // 2):
#         if str[i] != str[-i-1]:
#             ispalin = False
#             break
#         # j = len(str)-i-1
#         # if str[i]!=str[j]:
#         #     ispalin = False
#         #     break
#     print(ispalin)
#
#
# if __name__ == "__main__":
#
#     isPalindrom('mom')
