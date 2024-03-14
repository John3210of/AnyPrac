# https://school.programmers.co.kr/learn/courses/19344/lessons/242258
def solution(bandage, health, attacks):
    # attack 전까지 회복시간을 가지는데, 회복시간이 시전시간 이상이라면 추가회복량을 가진다.
    # 최대체력이상 받을수없다.
    # bandage는 [시전 시간, 초당 회복량, 추가 회복량]
    temp_time=0
    max_health=health
    for attack in attacks:
        heal_time = attack[0] - temp_time - 1
        heal_point = heal_time*bandage[1]
        if heal_time >= bandage[0]:
            heal_point+= bandage[2]*(heal_time//bandage[0])
        health+=heal_point
        if health>=max_health:
            health = max_health
        health -= attack[1]
        temp_time = attack[0]
        if health <= 0:
            return -1
    return health