class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        '''
        # backtracking? 결과는 unique 해야함
        # 같은 숫자를 여러번 사용할 수도 있다.
        # 근데 같은 수를 중복으로 써도 되서 그냥 dfs인거같기도?
        # 종료조건
            1. 숫자와 딱 맞을 경우 > answer append, return
            2. 숫자가 더 커질 경우 > return
        # 실행 순서
            1. 계산하려는 리스트에 원소를 순차적으로 추가
            2. 종료조건인지 확인하여 아니라면 재귀적으로 호출
            3. 호출이 종료되면 최근에 추가된 원소를 삭제
        '''
        answer_list=[]
        def backtracking(num_list,temp_sum,start):
            if temp_sum == target:
                answer_list.append(list(num_list))
                return
            elif temp_sum > target:
                return
            else:
                for i in range(start,len(candidates)): # 중복되는 수를 다시 안넣게 하기 위해
                    num_list.append(candidates[i])
                    backtracking(num_list,temp_sum+candidates[i],i)
                    num_list.pop()
        backtracking([],0,0)

        return answer_list
