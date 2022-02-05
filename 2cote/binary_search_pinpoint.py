lst = [-15, -14, -10, -5, 1, 2, 3, 4, 9, 13, 15, 24]
start=0
end = len(lst)
target=4
while start < end:
    mid = (start+end) // 2
    print('mid: ',mid)
    if lst[mid] < target:
        start = mid + 1
    elif lst[mid] > target:
        end = mid
    else:
        print(lst[mid])
        break





# print(len(lst))
# mid = len(lst) // 2
# cnt = 0
# while True:
#
#     if lst[mid] > n-1:
#         mid = len(lst[0:mid]) // 2
#         cnt += 1
#
#     elif lst[mid] < n-1:
#         mid = mid + len(lst[mid:]) // 2
#         cnt += 1
#
#     elif lst[mid] == n-1:
#         answer = n-1
#         print(answer)
#         break
#
#     if cnt >= len(lst) // 2:
#         answer = -1
#         print(answer)
#         break


# for i in range(len(lst)):
#     answer=-1
#
#     if i == lst[i]:
#         answer=i
#         break
#
# print(answer)
