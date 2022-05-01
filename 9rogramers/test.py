# from collections import deque
#
# def solution(people, tshirts):  # 5,6,10,11 만 안됨
#     answer = 0
#     people.sort()
#     tshirts.sort()
#     q=deque(people)
#     for i in tshirts:
#         if q[0]<=i:
#             answer+=1
#             q.popleft()
#     # for i in people:  5,6,10,11 만 됨
#     #     for j in tshirts:
#     #         if i<=j:
#     #             answer+=1
#     #             break
#
#     return answer

booked = [["09:10", "lee"]]
unbooked = [["09:00", "kim"], ["09:05", "bae"]]
for i in range(len(booked)):
    print(booked[i][0])
    booked[i][0]=booked[i][0].replace(':', '')
    print(booked[i][0])
