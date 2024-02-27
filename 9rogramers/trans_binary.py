# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def eliminate_zero(s):
    transed = []
    eliminated = 0
    for i in s:
        if i=='0':
            eliminated+=1
        else:
            transed.append(i)
    return transed,eliminated

s="110010101001"
count_trans = 0
eliminated_zero = 0
while True:
    if len(s)==1:
        break
    transed,eliminated = eliminate_zero(s)
    s=bin(len(''.join(transed)))[2:]
    eliminated_zero += eliminated
    count_trans+=1

print(count_trans)
print(eliminated_zero)