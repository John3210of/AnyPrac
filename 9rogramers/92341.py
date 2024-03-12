# https://school.programmers.co.kr/learn/courses/30/lessons/92341 주차요금계산
fees=[180, 5000, 10, 600]
records=["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

from collections import defaultdict
import math
def solution(fees, records):
    # 출차내역이 없다면 23:59를 기준으로 출차
    # fee 기본시간/기본요금 /단위시간/단위요금
    # records[i][:2] 시간 [3:5] 분 [6:10] 번호판 [11:] in,out
    # 시간을 계산해서 in에 입차시간 out에 출차시간 딕셔너리 만들기
    # 교집합이 없다면 입차시간 out을 23 59로 치환해서 넣어주기
    # 단위시간으로 나누어떨어지지않으면 올림
    # 차량번호가 작은순으로 정렬
    time_dict=defaultdict(int)
    in_out_check_dict = defaultdict(bool)
    fee_dict={}
    for record in records:
        if record[11:]=='IN':
            time_dict[record[6:10]]-=int(record[:2])*60+int(record[3:5])
            in_out_check_dict[record[6:10]] = True
        else:
            time_dict[record[6:10]]+=int(record[:2])*60+int(record[3:5])
            in_out_check_dict[record[6:10]] = False

    for k,v in in_out_check_dict.items():
        if v:
            time_dict[k]+=1439
            
    for number,time in time_dict.items():
        fee = fees[1]
        if time > fees[0]:
            fee+= math.ceil((time-fees[0])/fees[2])*fees[3]
        fee_dict[number] = fee
    sorted_list = [value for key, value in sorted(fee_dict.items())]
    return sorted_list