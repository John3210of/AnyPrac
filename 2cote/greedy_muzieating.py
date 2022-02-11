# 그럴바에 %로 나머지일때 빼게 만들면 될듯?
# 그런데 값이 0이되면 그냥 다음거를 빼야됨, 전부다 0이면 -1을 반환.
# k=3
#
# def eating(lst, cnt_down, cycle):  # [1, 0, 0]
#     point = 0
#     # 조금만더 많이씩 잘라주면됨 이분탐색으로 할수있을거같아
#     cut_len = cnt_down
#     total = sum(lst)
#     while True:
#         if total <= cut_len * len(lst):
#             if total + len(lst) > cut_len * len(lst):
#                 point = cut_len * len(lst)
#                 print('in while 1st break', cut_len)
#                 break
#             cut_len = cut_len - cut_len // 2
#             print('if cut_ren: ', cut_len)
#         elif total > cut_len * len(lst):
#             if total - len(lst) < cut_len * len(lst):
#                 point = cut_len * len(lst)
#                 print('in while 2nd break', cut_len)
#                 break
#             cut_len = cut_len // 2
#             print('elif cut_ren: ', cut_len)
#     print('point',point)
#     print('afterwhile cutlen: ', cut_len)
#
#     for i in range(len(lst)):
#         lst[i] -= cut_len
#     print(lst)
#     # if cnt_down-point < 0:
#     #
#
#
#
#     return lst
#
#
# def solution(food_times, k):  # k=cnt_down
#     if sum(food_times) - k < 0:
#         return -1
#     cycle = len(food_times)
#     return eating(food_times, k, cycle)
#
#
# food_times = [0, 1, 2]
# k = 1
#
# print(solution(food_times, k))

#######################################################################
# 그럴바에 %로 나머지일때 빼게 만들면 될듯?
# 그런데 값이 0이되면 그냥 다음거를 빼야됨, 전부다 0이면 -1을 반환.
k=3
def eating(lst, cnt_down, cycle):  # [1, 0, 0]
    pointer = 0
    for _ in range(cnt_down):
        while lst[pointer % cycle] == 0:
            pointer += 1
        lst[pointer % cycle] -= 1
        pointer += 1

    while lst[pointer % cycle] == 0:
        pointer += 1
    return pointer % cycle + 1


def solution(food_times, k):  # k=cnt_down
    if sum(food_times) - k <= 0:
        return -1
    cycle = len(food_times)
    return eating(food_times, k, cycle)