# 그럴바에 %로 나머지일때 빼게 만들면 될듯?
# 그런데 값이 0이되면 그냥 다음거를 빼야됨, 전부다 0이면 -1을 반환.

def eating(lst, cnt_down, cycle):  # [ 1, 0, 0]
    pointer = 0
    for _ in range(cnt_down):
        while lst[pointer % cycle] == 0:
            pointer += 1
        lst[pointer % cycle] -= 1
        pointer += 1
    if not '0' in lst:
        while lst[pointer % cycle] == 0:
            pointer += 1
        return pointer%cycle +1
    else:
        return -1


def solution(food_times, k):  # k=cnt_down
    # 2  0 1 2 3>0
    cycle = len(food_times)
    return eating(food_times, k, cycle)


food_times = [3, 2, 2]
k = 5

print(solution(food_times, k))
