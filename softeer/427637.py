import sys
from collections import deque
# pq?
# 짧은순 정렬을 하고 해보자
n = int(input())
lectures = []
for _ in range(n):
    lectures.append(list(map(int,(input().split()))))
lectures = sorted(lectures,key = lambda x: x[1])

start_time = 1
lecture_room = 0
for start, end in lectures:
    if start_time <= start:
        start_time = end
        lecture_room += 1
print(lecture_room)
    
import sys
import heapq
# pq?
'''
강의들을 시작 시간 기준으로 정렬한다.
우선순위 큐(힙)에 종료 시간을 저장하고, 현재 시작하는 강의가 기존 강의실에서 진행된 강의의 종료 시간 이후라면 해당 강의실을 재사용한다.
그렇지 않다면 새로운 강의실을 추가한다.
'''
n = int(input())
heap = []
for _ in range(n):
    start, end = map(int,input().split())
    heapq.heappush(heap,(end,start))

lecture_room = 0
time = 1

while heap:
    end,start = heapq.heappop(heap)
    if time <= start: 
        time = end
        lecture_room += 1

print(lecture_room)


    

