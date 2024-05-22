# https://www.acmicpc.net/problem/4889

import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
 # {}{}{}{{}{}}
def solution(order,case):
    stack=[]
    right_side=[]
    count=0
    for s in case:
        if s=='{':
            stack.append(s)
        else:
            if stack:
                stack.pop()
            else:
                right_side.append(s)
    result=right_side+stack
    if not result:
        return f'{order}. 0'
    for i in range(0,len(result),2):
        if result[i]+result[i+1]=="{{" or result[i]+result[i+1]=="}}":
            count+=1
        elif result[i]+result[i+1]=="}{":
            count+=2
        
    return f'{order}. {count}'

if __name__ == "__main__":
    # 중괄호의 열고닫음이 세트로 존재하는지를 봐야함.
    # 세트가 아닌것들끼리만 모아놓고, 한번더 바꿔주는 작업을한 횟수를 return
    cases=[]
    while True:
        exam=list(input().strip())
        if '-' in exam:
            break
        else:
            cases.append(exam)
    for i in range(len(cases)):
        print(solution(i+1,cases[i]))


'''
}{
{}{}{}
{{{}
{}{}{}{{}{}}
}{{{}{{}
---
'''