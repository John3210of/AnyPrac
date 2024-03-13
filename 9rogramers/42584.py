# https://school.programmers.co.kr/learn/courses/30/lessons/42584?language=python3 주식가격
stack=[]
prices =[1, 2, 3, 2, 3]
answer = [0]*len(prices)
for i,price in enumerate(prices):
    while stack and ((price < prices[stack[-1]]) or i==len(prices)-1): 
        idx = stack.pop()
        answer[idx]=i-idx
    stack.append(i)
print(answer)