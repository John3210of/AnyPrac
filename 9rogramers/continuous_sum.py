# https://school.programmers.co.kr/learn/courses/30/lessons/131701 연속 부분 수열 합의 개수

elements=[7,9,1,1,4]
org_len=len(elements)
elements=elements+elements
temp_sum=set()
for i in range(1,org_len+1): #순열의 길이
    for j in range(org_len): # 리스트 인덱싱
        temp_sum.add(sum(elements[j:j+i]))
print(len(temp_sum))