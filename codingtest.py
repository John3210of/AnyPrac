str = input()

                        #왜 palins 와 palins2를 나누어서 진행했는지 설명해주시면 좋을것 같습니다.
palins = []
palins2 = []

for i in range(len(str)):
    palin_count = 0
    for j in range(len(str)-i):
        if i-j >= 0 and i+j < len(str):
            if str[i-j] == str[i+j]:
                palin_count = palin_count + 1       #count의 변화를 아까처럼 한번 보여주시면 이해가 더 쉬울것 같습니다.
            else: break

    palins.append(palin_count)

## i와 i+1을 비교
for i in range(len(str)-1):
    palin_count = 0
    for j in range(len(str)-1-i):
        if i-j >= 0 and i+j+1 < len(str):
            if str[i-j] == str[i+j+1]:
                palin_count = palin_count + 1
            else: break
    palins2.append(palin_count)

##출력부
if max(palins) < max(palins2):
    middleidx = palins2.index(max(palins2))
    temp = max(palins2)
    print(str[middleidx-temp+1:middleidx+temp+1])

else:
    middleidx = palins.index(max(palins))
    temp = max(palins)
    print(str[middleidx-temp+1:middleidx+temp])


# h, w = map(int, input().split())
# n = int(input())
# arr = [[0 for col in range(w)] for row in range(h)]
#
# for i in range(n):
#     l, d, x, y = map(int, input().split())
#     if d == 0:
#         for j in range(l):
#             arr[x - 1][y - 1 + j] = 1
#     else:
#         for k in range(l):
#             arr[x - 1 + k][y - 1] = 1
#
# for row in range(h):
#     for col in range(w):
#         print(arr[row][col], end=" ")
#     print()
#
# # w,h,b =map(int,input().split()) #def
#
# # n = int(input())  #개수를 입력받아 n에 정수로 저장
# # d = [[0 for col in range(19)] for row in range(19)]
# #
# #
# # for i in range(n):
# #   x,y = map(int,input().split())
# #   d[int(x-1)][int(y-1)]=1
# #
# #
# #
# # # for i in range(n):
# #
# #
# #
# # for i in range(19):
# #   for j in range(19):
# #     print(d[i][j],end=" ")
# #   print()
# #
#
#
# #
# # d=[]        #d라는 이름의 빈 리스트 [ ] 변수를 만듦. 대괄호 기호 [  ] 를 사용한다.
# # for i in range(24):  #[0, 0, 0, ... , 0, 0, 0] 과 같이 24개의 정수 값 0을 추가해 넣음
# #  d.append(0)#각 값은 d[0], d[1], d[2], ... , d[22], d[23] 으로 값을 읽고 저장할 수 있음.
# #
# # for i in range(n):
# # d[a[i]] += 1
# # temp=a[0]
# # for i in range(1,n):
# # if temp<a[i]:
# # temp=temp
# # else:
# # temp=a[i]
# #
# # print(temp)
# #
# #
# #
# ## d = [list(map(int, input().split())) for _ in range(19)]
# # n = int(input())
# #
# # for _ in range(n):
# #     x, y = map(int,input().split())
# #     for j in range(19):
# #         if d[j][int(y-1)] == 0:
# #             d[j][int(y-1)] = 1
# #         else:
# #             d[j][int(y-1)] = 0
# #
# #         if d[int(x-1)][j] == 0:
# #             d[int(x-1)][j] = 1
# #         else:
# #             d[int(x-1)][j] = 0