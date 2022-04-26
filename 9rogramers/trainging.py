# def solution(n, lost, reserve):
#     lst = [1] * (n + 1)
#     for i in reserve:
#         lst[i] += 1
#     for i in lost:
#         lst[i] -= 1
#     # 1 0 2 0 2 1 //0 2 0 2 0 2 0 1 왼쪽부터 받아야함
#     for i in range(1, len(lst)):
#         if lst[i] == 0 and lst[i - 1] == 2:
#             lst[i] = 1
#             lst[i-1] = 1
#         elif lst[i] == 0 and lst[i + 1] == 2:
#             lst[i] = 1
#             lst[i+1] =1
#
#     answer = lst.count(1) + lst.count(2) - 1
#     return answer
def solution(n, lost, reserve):
    real_reserve = set(reserve) - set(lost)
    real_lost = set(lost) - set(reserve)
    print('real_reserve: ',real_reserve)
    print('real_lost: ',real_lost)
    lonely = []
    # for r in real_reserve:
    #     print('r-1 in real_reserve: ',r-1)
    #     print('r+1 in real_reserve: ',r+1)
    #     print('real_lost: ',real_lost)
    #     if not (r - 1 in real_lost) and not (r + 1 in real_lost):
    #         lonely.append(r)
    #         print('lonely: ',lonely)
    for r in real_lost:
        print('r-1 in real_reserve: ',r-1)
        print('r+1 in real_reserve: ',r+1)
        print('real_lost: ',real_lost)
        if not (r - 1 in real_reserve) and not (r + 1 in real_reserve):
            lonely.append(r)
            print('lonely: ',lonely)

    answer = n - len(lonely)

    return answer

n = 8
lost = [7, 2, 5, 6]
reserve = [1, 8, 4, 3]
print(solution(n, lost, reserve))
