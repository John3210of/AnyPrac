# https://school.programmers.co.kr/learn/courses/30/lessons/87390 n^2배열자르기

# 1 2 3 4 5 = > 123 223 333, l2 r3 > 32
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5

# n=3, n^2 길이의 리스트가 있고
# 2차원 위치 1> (0,0)// 2> (0,1) // 3> (0,2) , ... , 9(2,2) /
# left += 1
# right += 1
def solution(n, left, right): # 메모리초과
    answer = []
    count=1
    # count는 매라운드 증가하고 증가할때 i가 count보다 작거나 같으면 count로 채우기
    while count<=n:
        for i in range(1,n+1):
            if i <= count:
                temp=count
            else:
                temp=i
            answer.append(temp)
        count+=1
            
    return answer[left:right+1]

def solution(n, left, right):
    answer = []
    for i in range(left, right+1):
        row = i // n
        col = i % n
        answer.append(max(row, col) + 1)
    return answer