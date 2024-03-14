# https://school.programmers.co.kr/learn/courses/30/lessons/49993 스킬트리
def solution(skill, skill_trees):
    # skill = cbd 일때 %c%b%d 인지 확인. cbd는 필요충분 조건이 아님
    # c전에 b,d가 나오면 안됨 c-b-d를 stack에서 삭제
    answer = 0
    stack=[]
    for s in skill[::-1]:
        stack.append(s)
    for tree in skill_trees:
        temp_stack=stack[:]
        flag=1
        for t in tree:
            if t in temp_stack and t==temp_stack[-1]:
                temp_stack.pop()
            elif t in temp_stack and t!=temp_stack[-1]:
                flag=0
                break
        answer+=flag
    
    return answer