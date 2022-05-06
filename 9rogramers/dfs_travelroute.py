import collections
answer = []
graph = collections.defaultdict(list)

def dfs(s):
    while graph[s]:
        a=graph[s].pop(0)
        print('while graph[s] pop(0)',a)
        print('graph',graph)
        dfs(a)

    answer.append(s)
    print('if not graph : ',s)
    return

def solution(tickets):

    for a,b in tickets:
        graph[a].append(b)
        print('graph for first : ',graph)
    for a, b in graph.items():  #딕셔너리를 튜플형태로
        graph[a].sort()
        print('graph: for items ',graph)

    dfs("ICN")

    return answer[::-1]


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL","SFO"],["ATL", "ICN"]]
print(solution(tickets))