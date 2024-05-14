# https://leetcode.com/problems/zigzag-conversion/
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s
        graph=['' for _ in range(numRows)]
        # 한사이클에 2*(n-2)+2 개씩 들어감 > 2n-2
        # string을 사이클 단위로 쪼개서 마지막까지 반복시킴
        # cycle에서 0~n까지는 순차로 넣고, 이후에는 row-1을 하며 값을 추가함
        cycle=2*numRows-2
        start = 0
        while start < len(s):
            end = start + cycle if start + cycle <= len(s) else len(s)
            for i in range(start,end):
                if i-start<=numRows-1: # cycle 단위로 봐야함
                    graph[i-start]+=s[i]
                else:
                    graph[numRows-2-i+start]+=s[i]
            start = end
        answer=''
        for i in graph:
            answer+=i
        return answer