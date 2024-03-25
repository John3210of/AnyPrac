# 고득점키트 hash 다시풀어보기
def solution(nums): #폰켓몬
    dic={}
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    length=len(nums)//2
    return min(length,len(dic.keys()))
def solution(participant, completion): #완주하지 못한 선수
    dic={}
    for i in participant:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for c in completion:
        dic[c] -= 1
    
    for i,v in dic.items():
        if v==1:
            return i
def solution(phone_book): #전화번호 목록
    dic={}
    # 정렬하고, phone_book을 순회하면서
    # 현재 보고있는 애가 다른 번호의 접두어에 해당하는지
    phone_book.sort()
    for p in phone_book:
        for i in range(1,len(p)):
            pre=p[:i]
            if pre in dic:
                return False
        dic[p]=0
    return True
def solution(clothes): #의상
    dic={}
    for c in clothes:
        if c[1] in dic:
            dic[c[1]].append(c[0])
        else:
            dic[c[1]]=[c[0]]
    count=1
    for k,v in dic.items():
        count*=(len(v)+1)
    return count-1

def solution(genres, plays): # 베스트앨범
    answer = []
    # 전체합이 높으면 우선순위가 높음
    # 각 장르당 2개씩만 넣을 수 있음, 모든 장르는 2개 골라야함(1개라면 1개만)
    # 인덱스에 대한 정보도 필요함
    # 이중딕셔너리로?
    dic1 = {}
    dic2 = {}
    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))
        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p
    print(dic1)
    print(dic2)
    
    for (k, v) in sorted(dic2.items(), key=lambda x:x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x:x[1], reverse=True)[:2]:
            answer.append(i)
    print(answer)
    return answer

a=[1,2,3,45,6,7,8,9,10]
print(a[:22])