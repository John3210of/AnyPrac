from collections import deque
class Solution:
    def decodeString(self, s: str) -> str:
        # 재귀적으로 풀기? 
        # 시작조건은 [, 종료조건은 ]
        # 흠 순회하면서 스택? 푸는건가 ]를 만날때까지 돌고, 만나면 첫번째 [까지를 뽑아낸다.
        # 생각할 점 
        # 1. string형태라 2자리 이상의 정수가 있을경우
        # 2. 정수가 없을 경우
        num_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9'}
        s = deque(s)
        stack = []
        result=''
        while s:
            string = s.popleft()
            if string == ']':
                # [를 만날때까지 뽑아낸다.
                # 이렇게 하면 순서 보장이 안됨
                # 재귀로 푸는게 맞는듯? 전에 이렇게 풀었떤 문제 참고해보자 224번
                pass
            elif string in num_set:
                # 숫자있는곳 까지 그자리에서 뽑아낸다.
                pass