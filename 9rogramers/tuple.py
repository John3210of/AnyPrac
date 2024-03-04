# https://school.programmers.co.kr/learn/courses/30/lessons/64065?language=python3 튜플
import re
answer=[]
s="{{2},{2,1},{2,1,3},{2,1,3,4}}"
matches = re.findall(r'{([^}]*)}', s)
matches[0]=matches[0][1:]

set_list=[]
for m in matches:
    sub_set=list(map(int,m.split(',')))
    set_list.append(sub_set)
set_list.sort(key=len)

answer=[]
for sub in set_list:
    for j in sub:
        if j not in answer:
            answer.append(j)
print(answer)
