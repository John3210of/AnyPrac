# s = "[]()"

def is_vaild(s):
    pair = {
        '}': '{',
        ']': '[',
        ')': '('
    }

    opener = "{[("
    stack =[]

    for char in s:
        if char in opener:
            stack.append(char) #stack.push
        else:
            if not stack:
                return False
            top = stack.pop()
            if pair[char] != top:   #닫는 녀석
                return False

    return not stack    #짝이 맞다면 stack도 다 비어야 하기때문에


# 도전과제 리스트 안쓰고 stack.py로 만들어보기


assert is_vaild("{}()")  # 이럴경우 true를 반환
assert is_vaild("{[]}")
assert is_vaild("{[()]}")

assert not is_vaild("{}]")
assert not is_vaild("{{{{{{}}}}")

#빈 배열같은 경우 부정문을 입혔을때 true가 온다.
