# recursive > 함수 호출을 많이 할시, 오버헤드 커질 수 있다.
class Solution:
    def decodeString(self, s: str) -> str:
        def dfs(index):
            result = ""
            num = 0
            while index < len(s):
                char = s[index]
                if char.isdigit(): # 숫자를 만났을 때는 num을 갱신
                    num = num * 10 + int(char)
            # '['를 만나면 재귀적으로 탐색을 시작하고, 해당 결과값을 반복해서 추가
                elif char == '[': 
                    index, decoded_string = dfs(index + 1) 
                    result += decoded_string * num
                    num = 0  # num을 초기화
                elif char == ']':
                    return index, result # ']'를 만나면 현재까지의 결과를 반환
                else: # 일반 문자를 만났을 때는 결과에 추가
                    result += char
                index += 1
            return result
        return dfs(0)

# only stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_string = ""
        current_num = 0
        for char in s:
            if char.isdigit(): # 숫자인 경우, current_num에 더한다.
                current_num = current_num * 10 + int(char)
            elif char == '[':
                # 현재까지의 문자열과 숫자를 스택에 저장하고 리셋
                stack.append((current_string, current_num))
                current_string = ""
                current_num = 0
            elif char == ']':
                # 스택에서 이전 문자열과 숫자를 꺼내 현재 문자열을 반복한다.
                prev_string, num = stack.pop()
                current_string = prev_string + current_string * num
            else: # 문자라면 current_string에 더한다.
                current_string += char
        
        return current_string

# 두 풀이 모두 시간 공간 복잡도 O(N)