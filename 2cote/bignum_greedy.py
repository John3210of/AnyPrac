# 배열의크기 n 숫자 더하는횟수 m 연속하여 최대 k번까지 덧셈 가능
n, m, k = map(int, input('숫자 입력: ').split())

list1 = list(input('index 입력 (%d)개 : ' % n).split())

list1.sort()
print(list1)

list1_int = list(map(int, list1))

temp = 0
cnt = 0

for i in range(m):  # n=5, m=8, k=3
    # m회가 되었을때 더한 숫자를 출력한다.
    if cnt >= m: break

    for j in range(k):
        # 가장큰수를 k번 더하고 그 다음 큰수를 1번 더한다.
        if cnt >= m: break
        temp += list1_int[-1]
        cnt += 1

    temp += list1_int[-2]
    cnt += 1

result = temp
print(result)
