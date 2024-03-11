# https://school.programmers.co.kr/learn/courses/30/lessons/87946?language=python3 피로도
from itertools import permutations

k=80
dungeons=[[80,20],[50,40],[30,10]]
answer=0
# 순열 생성하여 출력
for perm in permutations(dungeons, len(dungeons)):
    j=k
    count=0
    for i,p in enumerate(perm):
        if j >= p[0]:
            j-=p[1]
            count+=1
    answer=max(answer,count)
print(answer)
