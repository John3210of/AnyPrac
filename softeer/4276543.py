import sys

'''
    수가 매우큼
    node, linked 는 아님
    외딴섬은 + 1
    회원수 n, 친분관계는 m, node에는 a,b의 친분관계
    이걸 완탐 안하고 할수가 있나?
'''
n, m = map(int,input().split())
weights = list(map(int,input().split()))
answer = 0
relations = {}
relation = set()
people = {}

for i in range(1,len(weights)+1):
    people[i] = weights[i-1]
    
for _ in range(m):
    person1,person2 = map(int,input().split())
    relation.add(person1)
    relation.add(person2)
    if person1 not in relations:
        relations[person1] = [people[person2]]
    else:
        relations[person1].append(people[person2])
    if person2 not in relations:
        relations[person2] = [people[person1]]
    else:
        relations[person2].append(people[person1])

for k,v in relations.items():
    if people[k] > max(v):
        answer += 1
answer += n - len(relation)
print(answer)