# Q3. 그룹 애너그램

# 조건1) 딕셔너리형태로 출력
from collections import Counter

# def groupAnagrams(list_word):
#
#     # 조건2) index의 문자열 count 하여 원소의 갯수체크
#     # 같다면 같은 딕셔너리로 들어가기 > 비효율적이다.
#     # 리스트 index 정렬하여 각 index가 같은지 비교하기.
#     # https://mong9data.tistory.com/33 sort sorted 차이점
#
#     new_lst = sorted(list_word)
#
#     print(new_lst)
import collections

from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = collections.defaultdict(list)

        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        print(anagrams)

        return anagrams.values()

# sorted()는 문자열도 잘 정렬하며 결과를 리스트 형태로 리턴하는데, 이를 다시 키로 사용하기 위해 join()으로 합쳐 이 값을 키로 하는 딕셔너리로 구성한다.
#
# ''.join(list())는 리스트를 문자열로 바꿔준다.

if __name__ == '__main__':
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))