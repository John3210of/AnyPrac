# https://school.programmers.co.kr/learn/courses/30/lessons/68645 삼각달팽이

def solution(n):
    direction = [(1,0),(0,1),(-1,-1)]
    answer = []
    n_list=[[0]*i for i in range(1,n+1)]
    row, col, count=-1,0,0
    # 아래>오른>위 순으로 움직이며, 방향전환의 한계는 n번까지 행해짐
    # 각 방향전환당 움직이는 횟수는 n으로부터 회전할때마다 1씩 줄어든다.
    for i in range(n):
        drow,dcol=direction[i%3]
        for j in range(i,n):
            row+=drow
            col+=dcol
            count+=1
            n_list[row][col]=count
    for i in n_list:
        answer.extend(i)
        
    return answer
