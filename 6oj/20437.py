import sys
input = sys.stdin.readline
from collections import defaultdict

def solution(s, k):
    if k == 1:
        print(1, 1)
        return
    
    char_positions = defaultdict(list)
    for idx, char in enumerate(s):
        char_positions[char].append(idx)
    
    shortest, longest = float('inf'), -1
    
    for char, positions in char_positions.items():
        if len(positions) >= k:
            for i in range(len(positions) - k + 1):
                length = positions[i + k - 1] - positions[i] + 1
                shortest = min(shortest, length)

                if s[positions[i]] == s[positions[i + k - 1]]:
                    longest = max(longest, length)
    
    if shortest == float('inf'):
        print(-1)
    else:
        print(shortest, longest)

if __name__ == "__main__":
    n = int(input())
    lst=[]
    for _ in range(n):
        s=input().strip()
        k=int(input())
        lst.append([s,k])
    if k==1:
        print(1,1)
    else:
        for s,k in lst:
            solution(s,k)


# def solution(s,k):
#     dic={}
#     target_s=[]
#     for i in s:
#         if i in dic:
#             dic[i]+=1
#         else:
#             dic[i]=1
#     for key,value in dic.items():
#         if value>=k:
#             target_s.append(key)
#     chars=find_repeated_chars(s,k,target_s)
#     chars.sort(key=len)
#     for char in chars:
#         if char[0]==char[-1]:
#             longest=char
#     if chars:
#         print(len(chars[0]),len(longest))
#     else:
#         print(-1)

# def find_repeated_chars(s,k,target_s):
#     answer=[]
#     for i in range(len(s)-1):
#         if s[i] in target_s:
#             temp=1
#             for j in range(i+1,len(s)):
#                 if s[j] == s[i]:
#                     temp+=1
#                     if temp==k:
#                         answer.append(s[i:j+1])
#     return answer
# 시간초과