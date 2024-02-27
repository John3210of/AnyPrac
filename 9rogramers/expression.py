#https://school.programmers.co.kr/learn/courses/30/lessons/12924
n=15
count=1
start=1
while (start <= n//2):
    temp=0
    for i in range(start,n//2+2):
        temp+=i
        if temp == n:
            count+=1
            start+=1
            break
        elif temp > n:
            start+=1
            break
if n==1:
    count=1
print(count)