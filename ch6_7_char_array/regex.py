# 정규표현식 (regular expression, regex)
# 문자열의 형식을 확인하는 식
# why use?
import re

if __name__ == "__main__":

    str = "The rain in Spain"

    x = re.search("^The", str)  # ^@ 는 @로 시작하는지를 의미함.

    str = "a@naver.com"
    x = re.search("r^[\w]", str)  # \w = alpha,num // \d = num // \s = space character ..
    print(x)
