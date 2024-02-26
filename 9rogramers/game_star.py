# https://school.programmers.co.kr/learn/courses/30/lessons/17682
import re

def separate_patterns(pattern):
    pattern_regex = r'(\d+[a-zA-Z]+|[*#])'
    separated = re.findall(pattern_regex, pattern)
    return separated

# 예시 문자열
s = "1D2S#10S"
scores = separate_patterns(s)
special = ['#','*']
bonus_dict={
    'S':1,
    'D':2,
    'T':3,
}
points=[]

for score in scores:
    if score in special:
        if score=='#':
            points[-1] *= -1
        else:
            points[-1] *= 2
            if len(points) >= 2:
                points[-2] *= 2
    else:
        if len(score) == 3:
            point = int(score[:2])
        else:
            point = int(score[0])
        bouns=score[-1]
        point **= bonus_dict[bouns]
        points.append(point)

print(sum(points))
