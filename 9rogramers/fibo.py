# https://school.programmers.co.kr/learn/courses/30/lessons/12945
# f_0 = 0
# f_1 = 1
# f_2 = f_0+f_1
# f_3 = f_1+f_2
# ...
# f_n = f_n_1+f_n_2

def fibo(n):
    fib = [0,1]
    for i in range(2,n+1):
        fib.append(fib[i-1]+fib[i-2])
    return fib[n]
n=5
print(fibo(n)%1234567)
