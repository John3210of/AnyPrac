# https://school.programmers.co.kr/learn/courses/30/lessons/17687?language=python3 n진수
# 진법n, 미리 구할 숫자의 갯수 t, 게임에 참가하는 인원 m, 튜브의 순서 p 가 주어진다.
def convert_to_base_n(number, base):
    if number == 0:
        return '0'
    result = ''
    while number > 0:
        number, remainder = divmod(number, base)
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(remainder - 10 + ord('A')) + result
    return result
n=16
t=16
m=2
p=2
number=''
for i in range(t*m+1):
    number+=convert_to_base_n(i,n)
answer=''
for j in range(p-1,len(number),m):
    answer+=number[j]
print(answer[:t])