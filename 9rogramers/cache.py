# https://school.programmers.co.kr/learn/courses/30/lessons/17680?language=python3 카카오 캐시

# 캐시사이즈는 상수이다.
# 캐시는 지나간 시간도 같이 가지고 있어야 한다.
# 도시 이름 리스트를 순회한다.
# 캐시에 존재하지 않는다면 실행시간에 5를 더한다.
# >>캐시 데이터의 크기가 캐시 사이즈보다 작다면 캐시에 데이터를 추가한다.
# >>>캐시데이터의 크기가 캐시 사이즈와 같다면 가장 오래된 데이터와 교체한다.
# 캐시에 존재한다면, 실행시간에 1을 더한다
cacheSize=3
cities=["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

cacheSize=2
cities=["Jeju", "Pangyo", "NewYork", "newyork"]
cacheData=[]
count=0
if cacheSize==0:
    count=5*len(cities)
else:
    for city in cities:
        city=city.lower()
        if city not in cacheData: # 존재하지 않을경우
            count+=5
            if len(cacheData)<cacheSize:  # 처음
                cacheData.append(city)
            else:                         # n개 이후
                cacheData.pop(0)
                cacheData.append(city)
        else:   # 존재할경우
            cacheData.remove(city)
            cacheData.append(city)
            count+=1
print(count)