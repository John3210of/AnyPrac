class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # bfs? dp?
        # 0이 언제 어디서 있을지몰라
        # 모든 경우의수를 볼 수 있나?
        # 0을 만날 경우에 얘를 넘어갈 수 있는지만 보는게?
        if len(nums)==1:
            return True
        if nums[-1] == 0:
            nums.pop()
        count = 0
        check_index = [0]
        for i in range(len(nums)):
            if nums[i] == 0:
                check_index.append(i)
                count += 1
        if count == 0:
            return True
        # 구간을 k,k+1 로 나눠서 이 구간의 어떤 nums[k] 값이 체크 인덱스의 인덱스를 넘을 수 있다면 pass
        # 만약 3 2 1 0 4 의 경우 i가 [0,3] 사이에서 nums[i]가 하나라도 4를 넘는 값이 나온다면 통과 가능
        # nums[check_index[k]] ~ nums[check_index[k+1]] 중에 하나라도 
        # check_index[k+1] - check_index[k] 값보다 큰게 있으면
        for i in range(len(check_index)-1):
            for j in range(check_index[i],check_index[i+1]):
                if nums[j] > check_index[i+1] - check_index[i]:
                    return True
        return False

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        for i in range(len(nums)):
            if i > farthest:
                # 현재 인덱스가 도달 가능한 최대 거리보다 크다면 더 이상 진행할 수 없음
                return False
            # 도달 가능한 가장 먼 거리 업데이트
            farthest = max(farthest, i + nums[i])
            if farthest >= len(nums) - 1:
                # 만약 도달 가능한 거리가 배열의 마지막 인덱스 이상이면 True 반환
                return True
        return False
