# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# 0과 1의 위치를 바꾼다, 없으면 1하나붙이고 0 하나붙이고
n = 78
b_n = list(bin(n)[2:])
while True:
    n+=1
    next_b_n=list(bin(n)[2:])
    if b_n.count('1') == next_b_n.count('1'):
        break
print(n)