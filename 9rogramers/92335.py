# https://school.programmers.co.kr/learn/courses/30/lessons/92335?language=python3 k진수에서 소수개수구하기

n=437674
k=3
def decimal_to_n(decimal_num,n):
    if decimal_num=='0':
        return '0'
    convert_str=''
    while decimal_num:
        convert_str+=str(decimal_num%n)
        decimal_num//=n
    return convert_str[::-1]

def is_prime(number):
    if number == 2:
        return True
    if number <= 1:
        return False
    if number%2 ==0:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
# 십진수를 n진수로 변환
# 0을 기준으로 split하여 리스트화
# 아리스토테네스의 채로 소수인지판단
s=decimal_to_n(n,k)
s_list=s.split('0')
count=0
for num in s_list:
    if num!='' and is_prime(int(num)):
        count+=1
print(count)

