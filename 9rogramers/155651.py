# https://school.programmers.co.kr/learn/courses/30/lessons/155651?language=python3 호텔대실
from collections import deque
def solution(book_time):
    # 겹치는 시간이 최대 몇개인지를 판단해야함
    # 시간을 정량화한다? 10분씩은 다 추가해야함.
    # book_time length만큼 방을 만들어놓고 각 list의 start time에 겹치는 요소가 몇개인지 체크한다.
    answer = 0
    booked=deque()
    for start,end in book_time:
        hh1,mm1=start.split(':')
        hh2,mm2=end.split(':')
        booked.append([int(hh1)*60+int(mm1),int(hh2)*60+int(mm2)+9])
    for _ in range(len(booked)):
        occupied=1
        temp_start,temp_end = booked.popleft()
        for start,end in booked:
            if start <= temp_start <= end:
                occupied+=1
        answer=max(occupied,answer)
        booked.append([temp_start,temp_end])
    return answer


# 다른풀이 imos법
CLEAR_TIME_DELTA = 10  # 예약된 회의가 끝난 후 몇 분 후에 회의실이 비워지는지를 나타내는 변수

def solution(book_time):
    """
    예약된 각 회의에 대해 최대 몇 개의 회의실이 필요한지 계산하는 함수

    :param book_time: 예약된 각 회의의 시작 및 종료 시간을 포함하는 리스트
    :return: 최대 회의실 수
    """
    imos = [0] * (24 * 60 + 10)  # 각 시간대별로 예약된 회의의 상태를 추적하기 위한 배열
    
    # 예약된 각 회의에 대해 imos 배열을 업데이트
    for start_time, end_time in book_time:
        start_minutes, end_minutes = time2minutes(start_time), time2minutes(end_time)
        imos[start_minutes] += 1
        imos[end_minutes + CLEAR_TIME_DELTA] -= 1
    
    cumulative_sum = 0  # 누적 합을 추적하는 변수
    max_rooms = 0  # 각 시간대에서 필요한 최대 회의실 수를 추적하는 변수
    
    # 각 시간대에 대해 누적 합을 계산하여 최대 회의실 수 업데이트
    for i in range(24 * 60):
        cumulative_sum += imos[i]
        max_rooms = max(max_rooms, cumulative_sum)
    
    return max_rooms

def time2minutes(time):
    """
    시간을 분으로 변환하는 함수

    :param time: 시간을 나타내는 문자열 (예: "15:30")
    :return: 분 단위로 변환된 시간
    """
    HH, MM = map(int, time.split(":"))
    return HH * 60 + MM

# 테스트용 예약된 회의 시간
book_time = [["15:00", "17:00"], ["16:40", "18:20"], ["14:20", "15:20"], ["14:10", "19:20"], ["18:20", "21:20"]]

# solution 함수 호출 및 결과 출력
print(solution(book_time))  # 출력: 3
