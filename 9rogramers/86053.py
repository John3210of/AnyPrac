# https://school.programmers.co.kr/learn/courses/30/lessons/86053 금과은 운반하기

def is_possible(time, a, b, g, s, w, t):
    n = len(g)
    total = 0
    total_g = 0
    total_s = 0

    for i in range(n):
        cnt = time // (2 * t[i])
        if time % (2 * t[i]) >= t[i]:
            cnt += 1

        tmp = min(cnt * w[i], g[i] + s[i])
        total += tmp
        total_g += min(tmp, g[i])
        total_s += min(tmp, s[i])

    if total >= a + b and total_g >= a and total_s >= b:
        return True
    return False

def solution(a, b, g, s, w, t):
    # 맞는 시간을 구하는건 아주 까다롭기 때문에 시간을 그냥 때려 맞추는 편이 나음
    # 2분탐색으로 아주 큰 수와 0을 시작 mid = lo+hi // 2
    # for문을 순회하며 총시간이 mid일때의 시간,금,은 운송량이 모두 기준치를 초과하는지에 대해 return
    # 운송량이 초과하면 hi=mid,부족하면 lo=mid로 보정을함
    # lo+1<hi 인 순간에 종료

    # 총 걸린 시간//왕복하는데 걸리는 시간 => 이동횟수
    # 딱코일경우 > 총 걸린시간을 왕복하는 시간으로 나눈 나머지가 1회 시간 이상이라면 1회 편도 추가
    # i번 회차에 운송한 양 = min(cnt*w[i],g[i]+s[i]) 
    # >> i번째 도시의 트럭이 옮길수 있는 최대무게 vs i번째 도시의 금+은의 무게중 작은값
    # 총 운송량 += i번 회차에 운송한양
    # 총 금 운송량 += i번 회차에 운송한양 vs 금의양중 작은값
    # 총 은 운송량 += i번 회차에 운송한양 vs 은의양중 작은값
    # 모든지표에서 이상이라면 return True, 아니라면 False
    hi = 400000000000000
    lo = 0

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if is_possible(mid, a, b, g, s, w, t):
            hi = mid
        else:
            lo = mid

    return hi