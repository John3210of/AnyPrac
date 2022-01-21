# Q33) 전화번호 문자조합. leecode 17

# 2에서 9까지의 숫자를 포함하는 문자열이 주어지면 숫자가 나타낼 수 있는 모든 가능한 문자 조합을 반환합니다. 어떤 순서로든 답을 반환하십시오.
# 전화 버튼과 마찬가지로 숫자 대 문자 매핑이 아래에 나와 있습니다. 1은 어떤 문자에도 매핑되지 않습니다.
# Constraints:
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9']

# 조건1) 2~9까지 숫자가 주어짐 >> 딕셔너리 형태로 {digit:'xxx'} 꼴로 리스트 선언해서 index에 접근할 수 있도록 하기.
# 조건2) 조합가능한 문자열 출력 >> depth가 1이므로 dfs보다 투포인터 포문을 사용하면 쉽겠지만 dfs로 접근.

def letterCombinations(digits):

    num_pad = {
        "2": ['a', 'b', 'c'],
        "3": ['d', 'e', 'f'],
        "4": ['g', 'h', 'i'],
        "5": ['j', 'k', 'l'],
        "6": ['m', 'n', 'o'],
        "7": ['p', 'q', 'r', 's'],
        "8": ['t', 'u', 'v'],
        "9": ['w', 'x', 'y', 'z'],
    }

    result = []
    if digits == "": #no input 예외처리
        return result

    ## 한개의 문자가 늘어날때마다 이전 결과까지 그룹시켜서 다시 경우의수 만들기
    for i in digits: #
        if result == []:    # 문자 하나인 경우
            result = num_pad[i]
        else:               # 문자 2개 이상인 경우
            temp = [] #문자가 하나 더 들어올때마다 초기화 할것.
            for j in result:
                for k in num_pad[i]:
                    print('temp_before',temp,'[j:',j,'] [k:',k,']')
                    temp.append(j + k)
                    print('temp_after',temp)

            result = temp # n번째까지의 경우의수 그룹화
        print('result :', result)

    print(result)
    return result


if __name__ == "__main__":
    letterCombinations('22544545')
