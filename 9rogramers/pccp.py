bandage = [5,1,5] # 시전시간 초당회복량 추가회복량 t x y
attacks =[[2, 10], [9, 15], [10, 5], [11, 5]] # 공격시간,피해량
health = 30 #체력 /최대체력이상불가능
max_health = health
pass_count = 0
time = attacks[-1][0]

# 시간은 흘러간다.
# 공격이 있는 시간이 아니라면 pass_count와 health상승한다. health는 최대체력이상 불가능, 공격 데미지가 현재 체력을 넘으면 return -1
next_attack = attacks.pop(0)
for i in range(1,time+1):
    print("*"*20)
    if next_attack[0] > i: # 공격이 없을 때
        pass_count += 1
        health += bandage[1]
        if pass_count >= bandage[0]:
            health += bandage[2]
        if health >= max_health:
            health = max_health
    else: # 공격 받았을때
        health -= next_attack[1]
        pass_count = 0
        if health <= 0:
            health = -1
            break
        else:
            if len(attacks) >=1 :
                next_attack = attacks.pop(0)
            else:
                print(health)
                break
    print(f'time : {i} , health : {health}')