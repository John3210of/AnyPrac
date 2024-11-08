class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 위상정렬 이것도 마찬가지로 음이 나오면 return [], ordering 도 필요함
        # 진입차수가 0인것으로 부터 시작하여 ordering 시킨다.
        # dic에는 과목들을 key로, 선행과목을 list의 value로
        course_dic = {i:[] for i in range(numCourses)}
        course_count = {i:0 for i in range(numCourses)}
        order = []
        queue = []
        for target, needed in prerequisites:
            course_count[target] += 1
            course_dic[needed].append(target)
        for k,v in course_count.items():
            if v == 0:
                order.append(k)
                queue.append(k)
        # 선행과목이 없는 과목부터 시작한다. 
        # 여기서 course_dic을 순회하며 이 과목이 선행인 다른 것들을 다음번에 수강할 과목으로 지정할 수 있다.
        # 만약 참조횟수가 음수가 된다면 서로가 서로의 선행과목이 되는 사이클이 존재하므로 리턴한다.
        while queue:
            s = queue.pop()
            for key in course_dic[s]:
                course_count[key] -= 1
                if course_count[key] < 0:
                    return []
                elif course_count[key] == 0:
                    queue.append(key)
                    order.append(key)
        if sum(course_count.values()) == 0:
            return order
        else:
            return []