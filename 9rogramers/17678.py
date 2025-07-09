from datetime import datetime, timedelta

def solution(n, t, m, timetable):
    '''
    셔틀 운행 횟수 n, 
    셔틀 운행 간격 t, 
    한 셔틀에 탈 수 있는 최대 크루 수 m, 
    크루가 대기열에 도착하는 시각을 모은 배열 timetable이 입력으로 주어진다.
    버스가 언제언제 오는지, 
    '''
    time_format = '%H:%M'
    bus_table = []
    start = datetime.strptime('09:00',time_format)
    bus_table.append(start)
    for i in range(n-1):
        start += timedelta(minutes=int(t))
        bus_table.append(start)
    time_table = []
    for tt in timetable:
        time_table.append(datetime.strptime(tt,time_format))
    print(time_table)

    return 1