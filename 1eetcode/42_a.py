# 문제 풀이 시에
# 기준점을 보고 왼쪽에서 가장 큰 값, 오른쪽에서 가장 큰 값을 구하고 그 중에 더 작은값 - 현재 가진 값을 칸마다 채울 수 있다.
# 이때, 음수값은 0을 채운다고 생각해도 된다. 
# T.C >O(n), S.C > O(n)


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