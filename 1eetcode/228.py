class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        idx = 0
        cnt=0
        # while idx < len(nums):
        while cnt < len(nums):
            cnt+=1
            temp = nums[idx]
            for i in range(idx+1,len(nums)):
                if temp + 1 == nums[i]:
                    temp += 1
                else:
                    idx = i-1
                    break
            if temp == nums[idx]:
                result.append(str(temp))
            else:
                result.append(str(nums[idx])+'->'+str(temp))
            print(result)
        return result

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # 리스트를 한번 순회
        # 연속된 구간의 인덱스를 구해야함
        # 연속된 구간인지는 현재와 다음값을 비교하여 + 1이라면 연속
        # 연속이 아니라면 [현재인덱스 - 연속된 구간,현재 인덱스]를 list에 넣음
        # 마지막 인덱스의 경우 바로 리스트에 넣고 종료
        offset = 0
        output = []
        for i in range(len(nums)):
            if i == len(nums)-1 or nums[i]+1 != nums[i+1]:
                output.append([nums[i-offset],nums[i]])
                offset = 0
            else:
                offset += 1
        answer = []
        for start, end in output:
            if start == end:
                answer.append(str(start))
            else:
                answer.append(str(start)+'->'+str(end))
        return answer