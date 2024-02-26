import re
s = "3people unFollowed me"
def solution(s):
    s_list = s.split(' ')
    pattern = r'^[0-9]'
    answer = ''
    for word in s_list:
        if word and re.match(pattern, word[0]):
            if len(word) > 1:
                answer += word[0] + word[1:].lower() + ' '
            else:
                answer += word + ' '
        else:
            if len(word) > 1:
                answer += word[0].upper() + word[1:].lower() + ' '
            else:
                answer += word.upper() + ' '
    return answer[:-1]
print(solution(s))