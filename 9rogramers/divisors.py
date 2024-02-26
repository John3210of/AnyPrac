# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def count_divisors_num(num):
    divisors=[]
    for i in range(1,num//2+1):
        if num%i==0:
            divisors.append(i)
    return len(divisors)+1

left =13
right =17
answer=0
for i in range(left,right+1):
    temp=count_divisors_num(i)
    if temp%2==0:
        answer+=i
    else:
        answer-=i
print(answer)