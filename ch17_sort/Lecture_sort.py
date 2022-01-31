# 버블 정렬은 idx-1번 반복한다.
# 이중 for문으로 n-1!만큼 반복시킨다.

# 선택 정렬

lst = [2, 5, 7, 3, 4, 9, 1]  # len=7 // idx0~6


def bubble(lst):
    bound=len(lst)-1
    for _ in range(len(lst)-1):
        for i in range(bound):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        bound -=1

    print(lst)


print()
print()
print()
print()
print()
print()
bubble(lst)


def select(lst):
    # 이중포문으로 0 >1~len(lst)까지 비교하여 가장 작은 값의 idx와 idx i 스왑 반복.
    for i in range(len(lst) - 1):
        small = lst[i]  # small 초기화
        for cur in range(i + 1, len(lst)):
            if small > lst[cur]:
                small = lst[cur]  # 최소값 갱신
                temp = cur  # 후에 swap 해줄 idx 갱신

        if lst[i] > small:  # swap
            lst[i], lst[temp] = lst[temp], lst[i]

    print(lst)


# select(lst)


def insertionsort(lst):
    # 0번째 요소는 이미 정렬되어있으니, 1번째 ~ lst(len)-1 번째를 정렬하면 된다.
    for cur in range(1, len(lst)):
        # 비교지점이 cur-1 ~ 0(=cur-cur)까지 내려간다.
        for delta in range(1, cur + 1):
            cmp = cur - delta
            if lst[cmp] > lst[cmp + 1]:
                lst[cmp], lst[cmp + 1] = lst[cmp + 1], lst[cmp]
            else:
                break
    return lst
