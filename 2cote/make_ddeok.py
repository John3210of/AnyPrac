# 떡의갯수 N, 요청한 떡의 길이 M
# list=[떡1len,떡2len,떡3len,...떡N_len]
# 일괄적으로 떡의 길이를 x 만큼 잘라서 나머지 만큼을 더해서 최소 M은 나올수있게 하기
# list[0]-x + list[1]-x+ ... + list[N-1]-x >= M 을 만족하는 최대 x를 구해라.
# 음수일경우 0을 반환.

# 원하는 idx가 list에 있는 idx라면 어떻게할건지?? 는 최대한 자를거니까 상관없나

n = 8
m = 9
lst = [10, 4, 7, 6, 2, 3, 5, 5]
lst.sort()
# 이진탐색이니까 가운데부터 드가자
cut = lst[n // 2]
print('초기 cut: ', cut)

while True:

    target = []
    print('target ini: ',target)
    sum_cut = 0
    for i in lst:
        if i > cut:
            target.append(i)
    print('target appended: ',target)
    for i in target:
        sum_cut += i - cut
    print('sum_cut: ', sum_cut)
    print('*' * 30)
    # 1/2씩 잘라 나가면서 up & down 을 판별.

    if sum_cut > m:  # 떡을 더 잘라야 할때
        if sum_cut - len(target) < m:  # lst = [0,0,0,2,3,3,5,5] m=1일때 cut=4
            print('애매한 cut: ', cut)
            print('*' * 30)
            break
        cut = cut + cut // 2
        print('더잘라 cut: ', cut)

    elif sum_cut < m:  # 떡을 덜 잘라야 할때
        cut = cut - cut // 2
        print('덜잘라 cut: ', cut)

    else:  # 딱맞을때
        print('딱맞아 cut: ', cut)
        print('*' * 30)
        break
    print('*' * 30)

# while True:
#     temp = 0  # temp = 잘린떡의 길이의 합
#     for i in list:
#         if i - cut < 0:
#             temp += 0
#         else:
#             temp += i - cut
#         print('temp: ', temp)
#
#     if temp > m:
#         cut += 1
#         print('ifcut:', cut)
#         print('iftemp: ', temp)
#     elif temp < m:
#         cut -= 1
#         print('elifcut:', cut)
#         print('eliftemp: ', temp)
#     else:
#         print('cut:', cut)
#         break
