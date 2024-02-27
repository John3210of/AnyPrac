# https://school.programmers.co.kr/learn/courses/30/lessons/12973
# 덩어리를 끝까지 찾아
# 같다면 덩어리를 찾아 다르면 그다음 인덱스부터 다시시작해
# dfs가 아니고 stack을 사용해야함 
# s=s[:start_idx]+s[end_idx+1:] 이부분에서 효율성 문제에 걸림
# def search_mass(idx,string):
#     if len(string) <= idx+1 or string[idx] != string[idx+1]:
#         return idx
#     elif string[idx] == string[idx+1]: 
#         return search_mass(idx+1,string)
# s='baabaa'
# start_idx=0
# while True:
#     if len(s) <= start_idx+1 or len(s)==0: # 끝까지 갔을때 그만
#         break
#     end_idx = search_mass(start_idx,s)
#     if start_idx == end_idx:
#         start_idx+=1
#     else:
#         s=s[:start_idx]+s[end_idx+1:]
#         start_idx=0
# if s=='':
#     answer=1
# else:
#     answer=0

s='baabaa'
stack=[]
for i in s:
    if stack and i==stack[-1]: # 같으면
        stack.pop()
    else: # 다르면
        stack.append(i)
