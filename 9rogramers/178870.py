# https://school.programmers.co.kr/learn/courses/30/lessons/178870 연속된부분수열의합
# 비정렬이라는건 크기가 같은 원소가 존재할 수도 있다는것인데 표현이 좀 이상하다.
def find_min_element(answer):
    min_diff = float('inf')
    min_element = None
    for x, y in answer:
        diff = abs(y - x)
        if diff < min_diff or (diff == min_diff and x < min_element[0]):
            min_diff = diff
            min_element = [x, y]
    return min_element
def solution(sequence, k):
    # sequence는 비정렬된 리스트
    # 가장 길이가 짧은
    # 완전탐색
    # 누적합이 작으면 이중 탐색, 같거나 크면 다음루프로
    # answer를 길이순서, 길이가같다면 인덱스의 첫번째가 작은순서로 정렬
    answer = []
    total = 0
    start = 0
    for end in range(len(sequence)):
        total += sequence[end]
        while total > k and start <= end:
            total -= sequence[start]
            start += 1
        if total == k:
            answer.append([start, end])
    return find_min_element(answer)