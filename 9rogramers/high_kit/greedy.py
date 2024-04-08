#1. 체육복
def solution(n, lost, reserve):
    # stack처럼 꺼내는데, 우측먼저 보는 식으로 하면 가장 효율적일듯
    # 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다> 빌려줄 수 없다.
    # 해서 n-len(losted) 를 return
    lost.sort()
    reserve.sort()
    losted=[]
    intersection = list(set(lost) & set(reserve))
    for item in intersection:
        lost.remove(item)
        reserve.remove(item)
    while lost:
        temp=lost.pop()
        if temp + 1 in reserve:
            reserve.remove(temp + 1)
        elif temp - 1 in reserve:
            reserve.remove(temp - 1)
        else:
            losted.append(temp)
    return n-len(losted)

#2. 조이스틱
# 이게 왜 그리디인지도 모르겠고 걍 모르겠음.. 다시 풀어보고 모르면 답보고 이해할래
def solution(name):
    # A-Z 까지 아스키코드로 변환해서 숫자의 차이가 적은쪽으로 이동시킴
    # 맨처음 커서는 가장왼쪽, 디폴트는 A로 잡혀있음.
    # 각 칸수별로 몇번 옮겨야 하는지 세기
    # A인 구간을 피해서 이동하는데 A-A의 길이가 가장 긴만큼 빼면 될듯?
    # A=65, Z=90, offset 65로 두고 0~25까지 0~12 0~12 13개 // 13~25 13~1
    if set(name)=={'A'}:
        return 0
    ascii=[i for i in range(13)]+[12-i for i in range(-1,12)]
    target=[]
    count=0
    max_count=0
    for n in name:
        temp=ascii[ord(n)-65]
        target.append(temp)
        
    return target
