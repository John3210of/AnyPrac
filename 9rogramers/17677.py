# https://school.programmers.co.kr/learn/courses/30/lessons/17677 뉴스클러스터링

import re
from collections import Counter

# 정규표현식으로 전환하는 코드
# 정규 표현식으로 바꿀 대상이 2글자씩의 원소를 가지는 리스트
# 65536 곱하고 소수점 버리는 코드
# 유사도는 (교집합/합집합) 으로 구함
# 딕셔너리로 만들고 겹칠때 더 작은 수를 교집합으로 보고 두개의 counter를 합치고 교집합을 한번빼면

def cut_and_append(text):
    lst = []
    for i in range(0, len(text)):
        substr = text[i:i+2]
        if re.match("^[a-zA-Z]+$", substr) and len(substr)>1:
            lst.append(substr.lower())
    return lst

def solution(str1, str2):
    intersection_count=0
    str1_dic,str2_dic=Counter(cut_and_append(str1)),Counter(cut_and_append(str2))
    if not str1_dic and not str2_dic:
        return 65536
    for k,v in str1_dic.items():
        if k in str2_dic:
            intersection_count+=min(v,str2_dic[k])
    union_count=sum(str1_dic.values())+sum(str2_dic.values())-intersection_count
    answer=int((intersection_count/union_count)*65536)

    return answer