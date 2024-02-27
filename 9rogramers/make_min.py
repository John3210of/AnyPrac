# https://school.programmers.co.kr/learn/courses/30/lessons/12941?language=python3
A = [1, 4, 2]
B = [5, 4, 4]

A.sort()
B.sort(reverse=True)
temp=0
for i in range(len(A)):
    temp += A[i]*B[i]
print(temp)