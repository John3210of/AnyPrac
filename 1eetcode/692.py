# https://leetcode.com/problems/top-k-frequent-words/
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 딕셔너리 > k이상 사전순 정렬?
        words_dict={}
        for word in words:
            if word not in words_dict:
                words_dict[word]=1
            else:
                words_dict[word]+=1
        result=[]
        for key,value in words_dict.items():
            result.append([key,value])
        result.sort(key=lambda x:(-x[1],x[0]))
        answer=[]
        for key,value in result:
            answer.append(key)
        return answer[:k]
