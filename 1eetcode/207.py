# https://m.blog.naver.com/ndb796/221236874984
# 위상정렬의 풀이
'''
① 진입차수가 0인 정점을 큐에 삽입합니다.
② 큐에서 원소를 꺼내 연결된 모든 간선을 제거합니다.
③ 간선 제거 이후에 진입차수가 0이 된 정점을 큐에 삽입합니다.
④ 큐가 빌 때까지 2번 ~ 3번 과정을 반복합니다. 
모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재하는 것이고, 
모든 원소를 방문했다면 큐에서 꺼낸 순서가 위상 정렬의 결과입니다.

진입차수
0   1

0   1 이면 0인곳에서 0을 큐에 넣고, 연결된노드의 간선을 모두 제거
그에 따라 진입차수도 같이 제거
진입차수가 0인곳에서 연결된 노드 모두 제거

노드의 간선을 저장할 dictionary로
순환참조를 관리할 dict
근데 순환참조라는 개념으로 볼때는 그냥 진입차수가 -1이 되는 순간이 아닐까
'''
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 순환참조가 되면 return false? a>b>c>a 이런식으로 되면 안됨
        # hint : 위상정렬?
        entry_count_dic = {i:0 for i in range(numCourses)}
        node_dic = {i: [] for i in range(numCourses)}
        for start, arrive in prerequisites:
            entry_count_dic[start] += 1
            node_dic[arrive].append(start)
        queue = deque()
        for k,v in entry_count_dic.items():
            if v == 0:
                queue.append(k)
        while queue:
            s = queue.pop()
            for key in node_dic[s]:
                entry_count_dic[key] -= 1
                if entry_count_dic[key] < 0:
                    return False
                elif entry_count_dic[key] == 0:
                    queue.append(key)
        if sum(entry_count_dic.values()) == 0:
            return True
        return False
 # 시간복잡도 o(V+E)
 # 공간복잡도 o(V+E)