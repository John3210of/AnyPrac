#https://school.programmers.co.kr/learn/courses/30/lessons/152996

from collections import defaultdict
weights = [100,180,360,100,270]
toc = [2,3,4]
answer = 0
info = defaultdict(int)
for w in weights:
    print('*'*10)
    answer += info[w] + info[w*2] + info[w/2] + info[(w*2)/3] + info[(w*3)/2] + info[(w*4)/3] + info[(w*3)/4]
    info[w] += 1
    print(info)
    

print(answer)
