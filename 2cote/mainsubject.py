import sys
input=sys.stdin.readline

n = int(input())
lst = []

for i in range(n):
    name, guk, yo, su = input().split()
    Guk = int(guk)
    Yo = int(yo)
    Su = int(su)
    lst.append([name, Guk, Yo, Su])

lst.sort(key=lambda x: (-x[1], x[2], -x[3], x[0])) # 무친 덱압축 -x[1] 이거 str 에러 때문에 구글링 하다가 찾음

for i in range(len(lst)):
    print(lst[i][0])

# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로
# 단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.
