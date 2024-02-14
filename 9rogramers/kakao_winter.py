# https://school.programmers.co.kr/learn/courses/30/lessons/258712?language=python3

friends = ["muzi", "ryan", "frodo", "neo"]
gifts = ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"]

def calculate_counts(table,gifts):
    for gift in gifts:
        gift = gift.split(" ")
        giver = friends.index(gift[0])
        getter = friends.index(gift[1])
        table[giver][getter] += 1
    return table

def calculate_gift_points(table):
    gift_points=[]
    for i in range(len(table)):
        gift_points.append(sum(table[i]))

    for j in range(len(table)):
        for k in range(len(table)):
            if j!=k:
                gift_points[j] -= table[k][j]
    return gift_points

def solution(friends,gifts):
    
    # create table
    table = []
    for i in range(len(friends)):
        table.append([0] * len(friends))

    # calculate gifts
    table = calculate_counts(table,gifts)

    # calculate_gift_points
    gift_points = calculate_gift_points(table)

    next_month=[0]*len(table)

    # 선물을 받는 조건  = > 선물을 더 많이 줬거나, 주고받지 않았을시에는 선물점수로. 여기서 같다면 서로 주고받지 않음.
    for i in range(len(table)):
        for j in range(i+1,len(table)):
            if table[i][j] > table[j][i]:
                next_month[i] += 1
            elif table[i][j] < table[j][i]:
                next_month[j] += 1
            else:
                if gift_points[i] > gift_points[j]:
                    next_month[i] += 1
                elif gift_points[i] < gift_points[j]:
                    next_month[j] += 1
    return max(next_month)

print(solution(friends,gifts))
