# Q2. 가장 흔한단어?

import re
from collections import Counter

def mostCommonword(str,ban):

    # 조건2) 대소문자 구분x, 특수문자 건너뜀 >> 소문자로 통일 , 특수문자 건너뜀
    temp = str.lower()
    temp = re.sub("[^a-z0-9]", " ", temp)

    # 조건1) 띄어쓰기를 기준으로 입력값 구분 >> 공백 기준으로 list에 넣기
    # https://wikidocs.net/14055
    list_str = temp.split()
    # print(list_str)

    # 조건3) 금지문자 설정 >> 조건문으로 금지문자 list에서 날리기
    #https://latte-is-horse.tistory.com/200

    list_str.remove(ban)

    # 조건4) 가장 많이 쓴 단어 출력 >> 같은 단어 count 하기
    # https://hashcode.co.kr/questions/233/%EB%A6%AC%EC%8A%A4%ED%8A%B8%EC%97%90%EC%84%9C-%ED%8A%B9%EC%A0%95-%EA%B0%92%EC%9D%B4-%EB%AA%87-%EB%B2%88-%EB%B0%98%EB%B3%B5%EB%90%98%EB%8A%94%EC%A7%80-%EC%95%8C%EC%95%84%EB%82%B4%EB%A0%A4%EB%A9%B4
    # https://developeryuseon.tistory.com/37 출력값 추출하기
    # https://dongdongfather.tistory.com/66 서식을 이용한 문자열 출력
    # result = Counter(list_str).values()

    cnt = Counter(list_str)
    result = cnt.most_common(1)[0][0]

    print('"%s"'%(result))

if __name__ == "__main__":
    print("문장,금지단어입력 :")
    paragraph = input().split('=')
    para = paragraph[1]
    banned = input().split('"')
    ban = banned[1]

    mostCommonword(para,ban)