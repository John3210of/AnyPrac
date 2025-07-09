from itertools import combinations,product
def is_candidate(user,banned):
    count = 0
    if len(user) != len(banned):
        return False
    for i in range(len(user)):
        if banned[i] =='*' or banned[i] == user[i]:
            count += 1
    return True if count == len(user) else False

def solution(user_id, banned_id):
    '''
    필터링된 문자열의 경우의 수
    조합
    banned id에 원소당 해당하는 것들을 넣는다. 문제는 중복인게 있어서 문제임
    그닥 크기가 크지 않긴해 그럼 다때려박고 횟수에 해당하는것의 수만 센다?
    # 아닌가 후보군을 먼저 구하는게 나은가
    중복후보군 어떻게 처리?
    	[('frodo',), ('fradi',)]
        [('crodo',), ('frodo',)]
        [('abc123', 'frodoc')]
        각  원소를 모두 1번씩 사용한 조합을 만든다.
    
    '''
    answer = 0
    banned_pile = 0
    banned_dic = {}
    banned_duplicate_dic = {}
    for b_id in banned_id:
        if b_id not in banned_dic:
            banned_duplicate_dic[b_id] = 1
            banned_dic[b_id] = set()
            banned_pile += 1
        else:
            banned_duplicate_dic[b_id] += 1
        for user in user_id:
            if is_candidate(user,b_id):
                banned_dic[b_id].add(user)
    temp = []
    for k,v in banned_duplicate_dic.items():
        temp.append(list(combinations(banned_dic[k],v)))

    for prod in product(*temp):
        temp_set = set()
        for p in prod:
            temp_set.add(p)
        if len(temp_set)==banned_pile:
            answer += 1

    return answer

from itertools import combinations, product

def is_candidate(user, banned):
    if len(user) != len(banned):
        return False
    for u, b in zip(user, banned):
        if b != '*' and u != b:
            return False
    return True

def solution(user_id, banned_id):
    banned_dic = {}            
    banned_duplicate_dic = {}  
    for b_id in banned_id:
        if b_id not in banned_dic:
            banned_dic[b_id] = set()
            banned_duplicate_dic[b_id] = 1
        else:
            banned_duplicate_dic[b_id] += 1
        for user in user_id:
            if is_candidate(user, b_id):
                banned_dic[b_id].add(user)
    
    temp = []
    for b, count in banned_duplicate_dic.items():
        if len(banned_dic[b]) < count:
            return 0
        temp.append(list(combinations(banned_dic[b], count)))
    
    valid_sets = set()
    
    for prod in product(*temp):
        candidate_set = set()
        for group in prod:
            candidate_set.update(group)
        if len(candidate_set) == len(banned_id):
            valid_sets.add(frozenset(candidate_set))
    
    return len(valid_sets)

from itertools import combinations, product
def is_candidate(user, banned):
    count = 0
    if len(user) != len(banned):
        return False
    for i in range(len(user)):
        if banned[i] == '*' or banned[i] == user[i]:
            count += 1
    return True if count == len(user) else False

def solution(user_id, banned_id):
    answer = 0
    banned_pile = 0
    banned_dic = {}
    banned_duplicate_dic = {}
    for b_id in banned_id:
        if b_id not in banned_dic:
            banned_duplicate_dic[b_id] = 1
            banned_dic[b_id] = set()
            banned_pile += 1
        else:
            banned_duplicate_dic[b_id] += 1
        for user in user_id:
            if is_candidate(user, b_id):
                banned_dic[b_id].add(user)
    temp = []
    for k, v in banned_duplicate_dic.items():
        temp.append(list(combinations(banned_dic[k], v)))
    
    
    valid_sets = set()  # 중복되는 최종 제재 집합을 제거하기 위한 집합
    for prod in product(*temp):
        candidate_set = set()
        # 기존 코드에서는 각 튜플을 그대로 집합에 추가했으나,
        # 여기서는 각 튜플 내부의 요소들을 평탄하게 추가합니다.
        for p in prod:
            candidate_set.update(p)
        # 각 banned_id 자리에 서로 다른 user_id가 할당되었는지 확인
        if len(candidate_set) == len(banned_id):
            valid_sets.add(frozenset(candidate_set))
    return len(valid_sets)
