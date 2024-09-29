from typing import List

class Solution:
    def check_strs(self,word,strs):
        for st in strs:
            if word != st[:len(word)]:
                return False
        return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        if '' in strs:
            return ''
        if len(strs)==1:
            return strs[0]

        for i in range(len(first_word)):
            if not self.check_strs(first_word[:i+1],strs):
                return first_word[:i]
        return first_word