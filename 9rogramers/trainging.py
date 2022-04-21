def solution(n, lost, reserve):
    lst = [1] * (n + 1)
    for i in reserve:
        lst[i] += 1
    for i in lost:
        lst[i] -= 1
    # 1 0 2 0 2 1 //0 2 0 2 0 2 0 1 왼쪽부터 받아야함
    for i in range(1, len(lst)):
        if lst[i] == 0 and lst[i - 1] == 2:
            lst[i] = 1
            lst[i-1] = 1
        elif lst[i] == 0 and lst[i + 1] == 2:
            lst[i] = 1
            lst[i+1] =1

    answer = lst.count(1) + lst.count(2) - 1
    return answer


n = 5
lost = [2, 4]
reserve = [1, 3, 5]
print(solution(n, lost, reserve))
