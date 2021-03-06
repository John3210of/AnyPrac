# Q12-38 // leetcode 332
# ticket[i] = [fromi, toi]가 한 항공편의 출발 및 도착 공항을 나타내는 항공권 목록이 제공됩니다.
# 일정을 순서대로 재구성하고 반환하십시오.
#
# 모든 티켓은 "JFK"에서 출발하는 남성의 것이므로 여정은 "JFK"로 시작해야 합니다.
# 유효한 여정이 여러 개인 경우 단일 문자열로 읽을 때 어휘 순서가 가장 작은 여정을 반환해야 합니다.
#
# 예를 들어, 여정 ["JFK", "LGA"]는 ["JFK", "LGB"]보다 사전 순서가 작습니다.
# 모든 티켓이 하나 이상의 유효한 일정을 구성한다고 가정할 수 있습니다. 모든 티켓은 한 번만 사용해야 합니다.

import collections

tickets=[['JFK','SFO'],['JFK','ATL'],['SFO','ATL'],['ATL','JFK'],['ATL','SFO']]

def findItinerary(tickets):
    graph = collections.defaultdict(list)
    print('graph:',graph)
    # 그래프 순서대로 구성
    for a, b in sorted(tickets):
        graph[a].append(b)
        print('graph[a]:',graph[a])
        print('b:',b)

    route = []

    def dfs(a):
        # 첫 번째 값을 읽어 어휘순 방문
        while graph[a]:
            print('while graph[a]:',graph[a])
            dfs(graph[a].pop(0))
        print('a:',a)
        route.append(a)
        print('route.append(a):',route)

    dfs('JFK')
    # 다시 뒤집어 어휘순 결과로
    print(route[::-1])
    return route[::-1]

if __name__ == "__main__":
    findItinerary(tickets)