# https://school.programmers.co.kr/learn/courses/30/lessons/12981?language=python3
n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]

game=[words.pop(0)]
order=2
cycle=1
for word in words:
    if word not in game and game[-1][-1] == word[0]: # 정상적으로 게임이 진행될 때
        game.append(word)
        order+=1
        if order > n:
            cycle+=1
            order=1
    else: # 걸렸을때
        answer = [order,cycle]
        