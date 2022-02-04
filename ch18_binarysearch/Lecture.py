# 파이썬에서는 바이너리서치를 지원한다.

# bisect << 이진탐색


import bisect
# bisect_left < 원하는 값이 여러개일경우, 가장 왼쪽에 있는
# 수의 idx를 반환한다.
def binary_search_builtin(nums, target):
    idx = bisect.bisect_left(nums, target)
    # idx == len(nums) 가능하기 떄문.

    if idx < len(nums) and nums[idx] == target:
        return idx
    else:
        return -1
