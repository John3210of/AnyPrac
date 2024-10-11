class Solution:
    def find_not_continuous(self, wall) -> int:
        # [1,2,3,4,5,6,7,8,9,10,11,12] > 12
        # [1,  3,4,  6,7,8,9,10,11,12] > 10
        status = []
        for i in range(len(wall)):
            if wall[i] == 1:
                status.append(i)
        return status[-1] - status[0] + 1 - len(status)

    def trap(self, height: List[int]) -> int:
        # layer마다 빈 구간을 찾는다. 빈 구간이란 1 0 1 과 같은 패턴을 말함
        # 1인곳의 위치와 0인곳의 위치를 뽑아내
        # [1,3,4,6,7,8,9,10,11] >> 2 5 처럼 연속하지 않은 구간이 몇칸인지를 찾아내
        # 318/323 메모리초과.. 거의다왔는디 
        max_height = max(height)
        walls = [[0 for _ in range(len(height))] for _ in range(max_height)]
        for wall in walls:
            for i in range(len(wall)):
                if height[i] > 0:
                    height[i] -= 1
                    wall[i] += 1
        count = 0
        for wall in walls:
            count += self.find_not_continuous(wall)
        return count
            