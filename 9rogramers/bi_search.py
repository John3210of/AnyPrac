# https://school.programmers.co.kr/learn/courses/30/lessons/86971 전력망을 둘로 나누기

# 모든  wires를 순회하면서 경우의 수를 따져봐야함
# wire는 단 한번 자를 수 있고, 잘랐을때 왼쪽 수에 연결된 모든 숫자의 갯수, 오른쪽에 연결된 모든 숫자의 갯수를 구하고 두 수의 차이를 구함
# 두수의 차이중에 가장 작은 값을 리턴함
# 연결된수는 wires를 순회하며 처음 숫자를 가지는 원소를 찾음
# 그 숫자를 가지는 원소의 다른 수를 가지고 있는 원소를 모두 찾음 
# >>이때 이미 방문했던곳은 다시 볼 필요가 없음
# >>그런식으로 모든 wire를 방문했다면 마침

n=9
wires=[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]
answer=[]

for i in range(len(wires)):
    visited=[0 for _ in range(len(wires))]
    visited[i]=1
    left,right = wires[i]
    left_set = set([left])
    right_set = set([right])
    while True:
        if sum(visited)==len(visited):
            break
        for j in range(len(wires)):
            if visited[j] == 0:
                dump=set(wires[j])
                if left_set.intersection(dump):
                    left_set.update(dump)
                    visited[j]=1
                elif right_set.intersection(dump):
                    right_set.update(dump)
                    visited[j]=1
    answer.append(abs(len(left_set)-len(right_set)))
print(min(answer))

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, rank, x, y):
    root_x = find(parent, x)
    root_y = find(parent, y)
    
    if root_x == root_y:
        return
    
    if rank[root_x] < rank[root_y]:
        parent[root_x] = root_y
    elif rank[root_x] > rank[root_y]:
        parent[root_y] = root_x
    else:
        parent[root_y] = root_x
        rank[root_x] += 1

def count_nodes(parent, n):
    counts = {}
    for i in range(n):
        root = find(parent, i)
        counts[root] = counts.get(root, 0) + 1
    return counts

def solution(n, wires):
    min_diff = float('inf')
    
    for i in range(len(wires)):
        parent = list(range(n))
        rank = [0] * n
        
        for j, (a, b) in enumerate(wires):
            if j != i:
                union(parent, rank, a - 1, b - 1)
        
        counts = count_nodes(parent, n)
        values = list(counts.values())
        diff = abs(values[0] - values[1])
        min_diff = min(min_diff, diff)
    
    return min_diff

# Test cases
print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))  # Output: 3
print(solution(4, [[1,2],[2,3],[3,4]]))  # Output: 0
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))  # Output: 1
