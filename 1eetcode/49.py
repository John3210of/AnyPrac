class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 정렬된 str을 dictionary의 key로, index 를 value로 O(n^2)
        dic={}
        for i in range(len(strs)):
            string = ''.join(sorted(strs[i]))
            if string not in dic:
                dic[string] = [strs[i]]
            else:
                dic[string].append(strs[i])
        answer=[]
        for key,strings in dic.items():
            answer.append(strings)
        return answer