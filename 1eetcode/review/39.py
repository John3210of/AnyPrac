class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 여러번 쓸 수 있고 조합은 유니크 해야함
        # 종료 조건은 target을 넘어섰을경우 혹은 값이 일치할 경우
        # 값이 일치하면 answer에 조합식을 넣기
        # 나머지 경우는 하나씩 백트래킹하면서 경우의수 따지기
        result=[]
        def _backtracking(temp,start):
            if sum(temp)>target:
                return
            elif sum(temp) == target:
                result.append(list(temp))   # append(temp) 로 하면 call by reference라 안됨
                return
            else:
                for i in range(start,len(candidates)):
                    candi = candidates[i]
                    temp.append(candi)
                    _backtracking(temp,i)   # unique해야 하고 중복선택이 가능하므로
                    temp.pop()
        _backtracking([],0)
        return result