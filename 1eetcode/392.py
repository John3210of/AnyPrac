from collections import deque
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        s=deque(s)
        for _t in t:
            if len(s) > 0 and s[0] == _t:
                s.popleft()
        return len(s)==0