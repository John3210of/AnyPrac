# https://school.programmers.co.kr/learn/courses/30/lessons/77885 2개 이하로 다른비트
def convert_to_base_n(number, base):
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        number, remainder = divmod(number, base)
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(remainder - 10 + ord('A')) + result
    return result

def solution(numbers):
    answer = []
    for num in numbers:
        if num % 2 == 0:
            answer.append(num + 1)
        else:
            binary_num = list('0'+convert_to_base_n(num, 2))
            for idx, val in enumerate(binary_num[::-1]):
                if val == '0':
                    binary_num[-idx-1] = '1'
                    binary_num[-idx] = '0'
                    break
            answer.append(int(''.join(binary_num), 2))
    return answer


print(solution([2,7]))