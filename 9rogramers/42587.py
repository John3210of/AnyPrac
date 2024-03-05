# https://school.programmers.co.kr/learn/courses/30/lessons/42587?language=python3 프로세스
from collections import deque

def solution(priorities, location):
    # 최대값을 빼야할 값으로 지정
    # 왼쪽부터 꺼내면서 최대값인지 확인
    # 최대값이라면 순서값(location) 과 몇번째로 나왔는지(count)를 확인하여 location과 같다면 count를 리턴
    # 최대값이 아니라면 locations와 priorities의 오른편에 다시 삽입
    # 다 나올때까지 반복
    locations=deque([i for i in range(len(priorities))])
    priorities=deque(priorities)
    count=0
    while priorities:
        target=max(priorities)
        temp,temp_order=priorities.popleft(),locations.popleft()
        if target==temp:
            count+=1
            if temp_order==location:
                return count
        else:
            priorities.append(temp)
            locations.append(temp_order)