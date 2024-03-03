# https://school.programmers.co.kr/learn/courses/30/lessons/12949 행렬의곱셈

def solution(arr1, arr2):
    answer = []
    # 행렬곱 => 1번째 arr의 n번째 행의 원소의 갯수만큼 덧셈이 이루어짐
    # 1번째 arr의 [n행] x 2번째 arr2의 [n열]의 합 = answer 의 (n,n) 의 값이 된다.
    # sum of arr1[x,i]*arr2[i,y]
    # 행렬곱은 [i*j] * [j*k] 의 형태로만 일어날 수 있다.
    # j만큼 덧셈이 일어나고, i만큼 행의 갯수,k만큼 열의 갯수가 된다.
    rows=len(arr1)
    cols=len(arr2[0])
    cal_count=len(arr1[0])
    for row in range(rows):
        row_list=[]
        for col in range(cols):
            total=0
            for i in range(cal_count):
                total+= arr1[row][i]*arr2[i][col]
            row_list.append(total)
        answer.append(row_list)
    return answer

 # 사실은 걍이렇게하면 생각할것도없긴함 ㅇㅇ;
import numpy as np

arr1 = np.array([[1, 4], [3, 2], [4, 1]])
arr2 = np.array([[3, 3], [3, 3]])

result = np.dot(arr1, arr2)
print(result)