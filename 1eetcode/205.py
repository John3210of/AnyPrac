class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # masking?
        dic = {}
        dic_2 = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = t[i]
            else:
                if dic[s[i]] != t[i]:
                    return False
        for i in range(len(s)):
            if t[i] not in dic_2:
                dic_2[t[i]] = s[i]
            else:
                if dic_2[t[i]] != s[i]:
                    return False
        return True