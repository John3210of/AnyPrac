# 시침은 2pi 43200초 2pi = 속 * 43200 >> 시침의속도 = 2pi / 12시간
# 분침은 2pi 3600초 2pi = 속 * 3600
# 초침은 2pi 60초 2pi = 속 * 60
# 거 = 속 * 시 > 2pi = 속 * 43200, 거리는 2pi*n + a 의 형태로 표기되고, 초침의 a와 시침/분침의 a가 같은 경우를 모두 세는것

## 1초마다 초침이 시침과 분침의 위치를 지나갔는지를 체크 하는식으로 하고, 00시와 12시를 지날경우 1개 빼야함 시분초침이 모두 겹친다
## 지금과 1초후를 비교하여 작았다가 커지는 순간이 오면 count ++ 1초후가 까지의 개념으로 적용
## 초침의 이전시간 기준 시침/분침보다 더 작고, 초침의 이후시간이 시/분침보다 더 크거나 같으면 겹친것으로 판단할 수 있다.

h1=0
m1=0
s1=0
h2=23
m2=59
s2=59

h1=1
m1=5
s1=5
h2=1
m2=5
s2=6

start_seconds = h1*3600 + m1*60 + s1
end_seconds = h2*3600 + m2*60 + s2

def calculate_pin_position(seconds):
    second_angle = (seconds % 60) * 6
    minute_angle = (seconds % 3600) / 10
    hour_angle = (seconds % 43200) / 120
    return hour_angle, minute_angle, second_angle

def count_pin_over(seconds,count):
    prev_h_pin, prev_m_pin, prev_s_pin = calculate_pin_position(seconds)
    next_h_pin, next_m_pin, next_s_pin = calculate_pin_position(seconds+1)
    if prev_s_pin < prev_h_pin: 
        if next_s_pin >= next_h_pin:
            count+=1
    if prev_s_pin < prev_m_pin:
        if next_s_pin >= next_m_pin:
            count+=1
    return count

count=0
if sum(calculate_pin_position(start_seconds)) == 0:
    count+=1
for i in range(start_seconds,end_seconds):
    count = count_pin_over(i,count)
print(count)


def get_cnt_from_midnight(h, m, s):
    h_degree = (h * 30 + m * 0.5 + s * 0.5 / 60) % 360
    m_degree = (m * 6 + s * 0.1) % 360
    s_degree = s * 6

    ret = -1
    if s_degree >= m_degree:
        ret += 1
    if s_degree >= h_degree:
        ret += 1

    ret += (h * 60 + m) * 2 
    ret -= h
    if h >= 12:
        ret -= 2 
    return ret

def solution(h1, m1, s1, h2, m2, s2):
    ret = get_cnt_from_midnight(h2, m2, s2) - get_cnt_from_midnight(h1, m1, s1)
    if (h1 == 0 or h1 == 12) and m1 == 0 and s1 == 0:
        ret += 1
    return ret