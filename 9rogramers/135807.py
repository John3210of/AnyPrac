# https://school.programmers.co.kr/learn/courses/30/lessons/135807?language=python3
def get_common_list(arrayN):
    arrayN.sort()
    n_common = arrayN[0]
    n_list=[]
    for i in range(1,n_common//2+1):
        if n_common % i == 0:
            n_list.append(i)
    n_list.append(n_common)
    result=[]
    for c in n_list:
        for i in range(len(arrayN)):
            if arrayN[i]%c != 0:
                break
            if arrayN[i]%c == 0 and i==len(arrayN)-1:
                result.append(c)
    return result

def solution(arrayA, arrayB):
    # 정렬된 a리스트의 0번 요소에 대한 약수를 모두 구한다.
    # 약수들을 돌리면서 모든 원소의 공통약수인 리스트를 구한다.
    # 정렬된 b리스트의 0번 요소에 대한 약수를 모두 구한다.
    # 약수들을 돌리면서 모든 원소의 공통약수인 리스트를 구한다.
    # 두 리스트를 비교하며 같지않은 수중에 가장 큰 값을 구한다.
    # 반대편의 모든수가 나누어 지지 않는 수중에 가장 큰 수
    
    # 14 = [1,2,7,14] => 7
    # 18 = [1,2,3,6,9,18] => 2,3,6
    # 10 => 1,2,5,10
    # 5 = >1,5
    a_list = get_common_list(arrayA)[1:]
    b_list = get_common_list(arrayB)[1:]
    print(a_list)
    print(b_list)
    answer=[]
    # a 배열의 공약수중에 b배열의 어떤수도 나누어 떨어지지 않는 수를 구해야함
    for a in a_list:
        for b in arrayB:
            if b%a==0:
                break
            if b%a!=0 and b==arrayB[-1]:
                answer.append(a)
    for b in b_list:
        for a in arrayA:
            if a%b==0:
                break
            if a%b!=0 and a==arrayA[-1]:
                answer.append(b)
    if not answer:
        return 0
    else:
        return max(answer)
