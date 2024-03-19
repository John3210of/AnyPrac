# https://school.programmers.co.kr/learn/courses/30/lessons/68936 쿼드압축후개수세기
def is_zipped(d2_lst,first_val):
    for i in d2_lst:
        for j in i:
            if first_val!=j:
                return False
    return True
def dfs(arr,dic):
    if len(arr)==1:
        return dic
    length=len(arr)//2
    left_top=[]
    right_top=[]
    left_bottom=[]
    right_bottom=[]
    for i in arr[:length]:
        left_top.append(i[:length])
        right_top.append(i[length:])

    for i in arr[length:]:
        left_bottom.append(i[:length])
        right_bottom.append(i[length:])

    if is_zipped(left_top,left_top[0][0]) and len(left_top)>1:
        dic[left_top[0][0]]-= (len(left_top)**2-1)
    else:
        dfs(left_top,dic)    

    if is_zipped(right_top,right_top[0][0]) and len(right_top)>1:
        dic[right_top[0][0]]-= (len(right_top)**2-1)
    else:
        dfs(right_top,dic)


    if is_zipped(left_bottom,left_bottom[0][0]) and len(left_bottom)>1:
        dic[left_bottom[0][0]]-= (len(left_bottom)**2-1)
    else:
        dfs(left_bottom,dic)
        
    if is_zipped(right_bottom,right_bottom[0][0]) and len(right_bottom)>1:
        dic[right_bottom[0][0]]-= (len(right_bottom)**2-1)
    else:
        dfs(right_bottom,dic)

    return dic
def solution(arr):
    # 2^n 형태의 정사각형을 4등분,4등분,4등분 ,.., 1칸이 될때까지 등분
    # 등분을 했을때 모두 같다면 숫자 하나로 압축.
    # dfs로 구현가능
    # 종료조건 칸에 들어간 숫자가 1개일때
    # 칸에 들어가 있는 모든수가 같다면 0또는 1 하나로 압축
    # 기존 1의개수와 0의개수를 업데이트 하는식으로. 4등분을 한 리스트의 크기-1 만큼 각 수의 개수가 줄어듬
    dic={0:0,1:0}
    for i in arr:
        for j in i:
            dic[j]+=1
    if dic[0]==0:
        return [0,1]
    elif dic[1]==0:
        return [0,1]
    else:
        dfs(arr,dic)
    return dic

arr=[[1,1,0,0],[1,0,0,0],[1,0,0,1],[1,1,1,1]]
arr=[[1,1,1,1,1,1,1,1],[0,1,1,1,1,1,1,1],[0,0,0,0,1,1,1,1],[0,1,0,0,1,1,1,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,0,0,1],[0,0,0,0,1,0,0,1],[0,0,0,0,1,1,1,1]]
print(solution(arr))