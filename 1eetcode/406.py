class Solution:
    # 전혀 모르겠음 문제가 무슨뜻이지
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        sol = []
        people.sort(key=lambda x: (-x[0], x[1]))
        print(people)
        for p in people:
            sol.insert(p[1], p)
            print(p)
        print(sol)