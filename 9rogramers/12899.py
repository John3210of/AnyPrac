# https://school.programmers.co.kr/learn/courses/30/lessons/12899 124나라의숫자

def convert(n,base):
    s=''
    while n>0:
        quo,remain=divmod(n,base)
        if remain==0:
            quo-=1
            remain=3
        s=str(remain)+s
        n=quo
    return s

def solution(n):
    # 진법변환시에
    # 나누어 떨어지면 몫에 -1을 하고 나머지에+3을 해준다.
    # 3은 4로 표기한다.
    answer=''
    string = convert(n,3)
    for s in string:
        if s=='3':
            s='4'
        answer += s
    return 
