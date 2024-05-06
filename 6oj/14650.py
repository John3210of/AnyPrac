# https://www.acmicpc.net/problem/14650
import sys
from itertools import product
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    # 조합을 이용해서 합이 3의 배수가 되면 count++
    numbers=[0,1,2]
    result=[]
    answers=[]
    count=0
    for comb in product(numbers,repeat=n):
        result.append(comb)
    for c in result:
        temp=''
        for i in range(len(c)):
            if i==0 and c[i]==0:
                break
            else:
                temp+=str(c[i])
        if temp !='':
            answers.append(int(temp))
    for ans in answers:
        if ans%3==0:
            count+=1
    print(count)