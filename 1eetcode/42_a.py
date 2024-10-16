# 기준점을 보고 왼쪽에서 가장 큰 값, 오른쪽에서 가장 큰 값을 구하고 그 중에 더 작은값 - 현재 가진 값을 칸마다 채울 수 있다.
# 이때, 음수값은 0을 채운다고 생각해도 된다. 

# T.C >O(n^2), S.C > O(n)
class Solution:
    # eq : min(max(height[:pointer]), max(height[pointer+1:])) - height[pointer]
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left],height[right]
        result = 0
        for i in range(1,len(height)-1):
            left_max, right_max = max(height[:i]), max(height[i+1:])
            temp_water = min(left_max,right_max) - height[i]
            if temp_water > 0:
                result += temp_water
        return result

# T.C >O(n), S.C > O(n)
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        result = 0
        left_max = [0] * n
        right_max = [0] * n
        left_max[0] = height[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], height[i])
        right_max[n-1] = height[n-1]
        for i in range(n-2, -1, -1):
            right_max[i] = max(right_max[i+1], height[i])
        for i in range(1, n-1):
            temp_value = min(left_max[i-1], right_max[i+1])
            temp_water = temp_value - height[i]
            if temp_water > 0:
                result += temp_water
        return result

# 이걸 T.C > O(n), S.C > O(1) 로 해결할 수 있는 방법이 있는데
# eq : min(lmax, rmax) - height[i], i : current index
# l_poiner 와 r_pointer를 옮기는 조건을 어떻게 잡을까?
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l_point, r_point = 0, len(height)-1
        l_max, r_max = height[l_point], height[r_point]
        ans = 0
        while l_point < r_point:
            if l_max <= r_max:
                pass
            else:
                pass