class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # upper lower
        # 비트처리 하듯이? 알파벳의 위치를 기억해두고서 뒤집으면?
        # 잘모르겠음..
        alpha_indexes = [i for i in range(len(s)) if s[i].isalpha()]
        answer=[]

        # masking해야하는 bit의 개수 = 2^n-1
        for bitmask in range(1<<len(alpha_indexes)):
            string = list(s)
            for i in range(len(alpha_indexes)):
                # 현재 마스킹할 위치에 해당하는 알파벳은 전부 upper로 
                if bitmask & (1<<i):
                    string[alpha_indexes[i]] = string[alpha_indexes[i]].upper()
                else:
                    string[alpha_indexes[i]] = string[alpha_indexes[i]].lower()
            answer.append(''.join(string))
        return answer