# Q1.유효한 팰린드롬인가?

def isPalindrom(str):  # 투포인터로 가는 방법도 있다.
    ispalin = True

    #excp) 대소문자 구별x
    str = str.lower()   # 반환형이 있는 함수이다.
    #excp) 영문과 숫자만 받기
    if not str.isalnum():
        return False

    for i in range(len(str) // 2):
        if str[i] != str[-i-1]:
            ispalin = False
            break
        # j = len(str)-i-1
        # if str[i]!=str[j]:
        #     ispalin = False
        #     break
    print(ispalin)


if __name__ == "__main__":

    isPalindrom('mom')
