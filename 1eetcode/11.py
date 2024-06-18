class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 걸러낼 값은 len(lst)*min(lst[0],lst[-1])
        # 넓이는 min(lst[n],lst[m])*(m-n)
        # 시간복잡도를 어케 줄이지
        # area=(len(height)-1)*min(height[0],height[-1])
        # for start in range(len(height)-1):
        #     for end in range(start+1,len(height)):
        #         area = max(min(height[start],height[end])*(end-start),area)
        # return area
        
        # 투포인터로 n으로 줄이기
        start=0
        end=len(height)-1
        area=0
        while start < end:
            area=max(area,(end-start)*min(height[start],height[end]))
            if height[start] >= height[end]:
                end-=1
            else:
                start+=1
        return area