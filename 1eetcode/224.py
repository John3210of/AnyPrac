class Solution:
    def calculate(self, s: str) -> int:
        # 괄호 때문에 어려울듯?
        # 기본은 기호를 만나기 전까지 혹은 마지막이면 숫자로 인식시키기
        # 여는괄호를 만나면 가장빠른 닫는괄호까지를 수식덩어리로 처리하는데
        # 괄호를 처리하기 위한 재귀함수를 만든다?
        def helper(index: int):
            current_result = 0
            current_number = 0
            sign = 1
            
            while index < len(s):
                char = s[index]
                
                if char.isdigit():
                    current_number = current_number * 10 + int(char)
                
                elif char == '+':
                    current_result += sign * current_number
                    current_number = 0
                    sign = 1
                
                elif char == '-':
                    current_result += sign * current_number
                    current_number = 0
                    sign = -1
                
                # 재귀로 내부의 괄호 세트부터 처리할 부분
                elif char == '(':
                    current_number, index = helper(index + 1)
                
                elif char == ')':
                    current_result += sign * current_number
                    return current_result, index
                
                index += 1
            
            current_result += sign * current_number
            return current_result, index
    
        result, _ = helper(0)
        return result
