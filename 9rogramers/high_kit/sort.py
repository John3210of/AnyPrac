# https://school.programmers.co.kr/learn/courses/30/lessons/42748 k번째수
def solution(array, commands):
    answer=[]
    for start,end,order in commands:
        answer.append(sorted(array[start-1:end])[order-1])
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/42746 가장 큰 수
def solution(numbers):
    # 원소의 길이는 최대 4자리 자리수는 최소1개
    answer=''
    numbers.sort(key = lambda x: int((str(x)*4)[:4]),reverse=True)
    if numbers[0]==0:
        return '0'
    for num in numbers:
        answer+=str(num)
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/42747 h-index
def solution(citations):
    n = len(citations)
    citations.sort()  # 오름차순으로 정렬
    h_index = 0
    for i in range(n):
        if citations[i] >= n - i:  # 논문의 수에서 현재 논문의 순서를 뺀 값보다 인용 횟수가 크거나 같으면 H-Index의 후보
            h_index = n - i
            break  # H-Index 후보를 찾으면 반복 종료
    return h_index
