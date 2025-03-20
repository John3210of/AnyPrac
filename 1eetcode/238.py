class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        본인을 제외한 나머지 곱
        o(n)으로 해결, 곱을 구한뒤 나누면 안됨
        hint 기준점으로부터의 왼쪽의(prefix) 모든곱과 오른쪽(subfix)의 모든곱을 구한다.
        '''
        prefix = [1 for _ in range(len(nums))]
        subfix = [1 for _ in range(len(nums))]
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]
        for i in range(len(nums)-2,-1,-1):
            subfix[i] = subfix[i+1]*nums[i+1]
        answer = []
        for i in range(len(nums)):
            answer.append(prefix[i]*subfix[i])
        return answer
 # 시간복잡도 O(n), 공간복잡도 O(n)