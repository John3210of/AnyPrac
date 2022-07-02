lottos = [44, 1, 0, 0, 31, 25]

win_nums = [31, 10, 45, 1, 6, 19]

cnt = 0  # 당첨된 번호의 갯수
molru = lottos.count(0)
for i in range(len(lottos)):
    if lottos[i] in win_nums:
        cnt += 1
# 0의 갯수 만큼 더 당첨될 수 있다.
# 그 중에 최고 겹치는수와 최고 안겹치는 수를 골라라.
lucky, unlucky = 0, 0
if cnt <= 1:
    unlucky = 6
elif cnt == 2:
    unlucky = 5
elif cnt == 3:
    unlucky = 4
elif cnt == 4:
    unlucky = 3
elif cnt == 5:
    unlucky = 2
elif cnt == 6:
    unlucky = 1

if unlucky - molru <= 1:
    lucky = 1
else:
    lucky = unlucky - molru

answer = [lucky, unlucky]
