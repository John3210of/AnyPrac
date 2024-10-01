from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        # 앞에서부터 순차적으로 output에 추가한다.
        # 이때, 숫자가 있는경우 숫자 뒤에는 []가 붙어있고, []안의 결과에 수를 곱한만큼 output에 더한다.
        # 재귀적으로, []안의 문자열을 분석한다.
        # [ 일 경우, 재귀적으로 탐색하고 이때 ]를 만나면, 더해줄 문자열과, 다음 탐색할 index를 반환한다.
        # 아 모르겠다 개어렵다
        # 문자를 순회하는 방법, 2자리 이상의 숫자가 나올때의 방법
        result=''
        def dfs(string,index):
            while index < len(s):
                if s[index] == '[':
                    sub,next_idx = dfs(string,index+1)
                    index = next_idx
                elif s[index] == ']':
                    result += sub
                    return result, index
                else:
                    index += 1
        result,index = dfs(s,0)
        return result