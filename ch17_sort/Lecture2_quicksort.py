# quick sort는 보편적으로 아주 좋은 기법이지만,
# 최악일때 n^2이 되므로 n log n 을 보장하는 merge,heap sort를 쓴다.
# 분할정복을 통해 주어진 배열을 정렬하는 알고리즘.
# divide and conquer
lst = [1, 2, 3, 4, 5, 6, 7, 8]


def qsort(lst):  # 피벗을 기준으로 왼편, 오른편을 각각 다시 분할화 해야함.
    def recur(lst, left, right):
        if left >= right:  # 종료 조건
            return
        pivot = lst[right]  # 현재 리스트의 가장 오른편 요소를 pivot으로 한다.
        cursor = left - 1  # 현재 커서의 위치
        for i in range(left, right):  # 현재 리스트를 돌면서 비교한다.
            if pivot < lst[i]:  # lst값이 더 클경우는 상관없음
                print('pass', lst)
            else:  # 더 작을 경우에 swap이 일어남
                cursor += 1  # swap해도 되는 값중에 가장 첫번째 값에 커서가 가게 만듬.
                lst[cursor], lst[i] = lst[i], lst[cursor]  # lst[i]가 스왑되야 할 경우,
                print('스왑', lst)  # 커서의 요소와 swap
        cursor += 1  # pivot 넣어줄 위치 조정
        lst[cursor], lst[right] = lst[right], lst[cursor]  # pivot을 제자리로 슛
        print('pivot 슛:', lst)
        recur(lst, 0, cursor - 1)  # pivot기준 좌로 계속
        recur(lst, cursor + 1, right)  # pivot기준 우로 계속

    recur(lst, 0, len(lst) - 1)
    print('완료', lst)
    return lst


qsort(lst)

# 마지막 원소를 pivot으로 잡는다.(기준점) 왜 마지막 원소를 해야됨??
#   >> 그렇게하나 저렇게하나 똑같음 걍 보기 편해서 인듯?

# lst = [1, 6, 4, 2, 5, 3]
#
#
# def qsort(lst):  # 재귀를 하려고 하니, 기준이 필요함
#     def recur(lst, start, end):
#         if start > end:
#             return
#         pivot = lst[end]
#         cursor = end
#         # cursor = -3
#         for i in range(len(lst) - 1):
#             if pivot < lst[i]:
#                 continue
#             else:  # 더 작을 경우
#                 cursor += 1
#                 lst[cursor], lst[i] = lst[i], lst[cursor]
#         cursor += 1
#         lst[cursor], lst[pivot] = lst[pivot], lst[cursor]
#         # cursor =>pivot의 위치
#
#         l_lst = lst[start:cursor - 1]
#         r_lst = lst[cursor + 1:end]
#
#         recur(l_lst, start, cursor - 1)
#         lst[start:cursor-1]=l_lst
#         recur(r_lst, cursor+ 1,end)
#         lst[cursor + 1:end]=r_lst
#         return lst
#
#     print('입력 ', lst)
#     recur(lst, 0, -1)  # 함수가 호출되면 시작해
#     print('완료', lst)
#
# qsort(lst)

# 여기서 좌 우로 다시 가야하는데, 그걸어떻게 주냐?
# 좌 집합 기준으로 다시 0~[cursor-2]까지 의 범위를 가지고 pivot=cursor-1로 퀵소트
# 우 집합 기준으로 다시 [cursor+1]~[-2]까지의 범위를 가지고 pivot=lst[-1]로 퀵소트

# qsort(lst)
# lst = [3, 4, 5, 6, 1, 2]
#######

# lst = [1, 6, 4, 2, 5, 3]
# pivot = lst[-1]
# # pivot = lst[-3]
# # 넣어줘야할 자리의 인덱스넘버 => 0부터 출발해서 더 큰값이 나왔을경우 그 자리를 바꿈
# cursor = -1
# # cursor = -3
# print('입력 ', lst)
# for i in range(len(lst) - 1):
#     if pivot < lst[i]:
#         print('pass', lst)
#     else:  # 더 작을 경우
#         cursor += 1
#         lst[cursor], lst[i] = lst[i], lst[cursor]
#         print('스왑', lst)
# cursor += 1
# lst[cursor], lst[-1] = lst[-1], lst[cursor]
#
# print('완료', lst)
# 여기서 좌 우로 다시 가야하는데, 그걸어떻게 주냐?
# 좌 집합 기준으로 다시 0~[cursor-2]까지 의 범위를 가지고 pivot=cursor-1로 퀵소트
# 우 집합 기준으로 다시 [cursor+1]~[-2]까지의 범위를 가지고 pivot=lst[-1]로 퀵소트

# qsort(lst)
