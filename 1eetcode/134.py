class Solution:
    # 결과적으로 이번 바퀴를 돌수 있냐? 를 확인하는것이 중요하다. 언제라도 cost를 초과한다면 False를 return
    def can_travel(self, index, gas, cost) -> bool:
        tank = gas[index]
        for _ in range(len(gas)//2):
            tank -= cost[index]
            if tank < 0:
                return False
            else:
                index += 1
                tank += gas[index]
        return True
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # 1. 현재 가스량이 증가됨
        # 2. 이동할곳의 코스트만큼 있는지를 확인, 가능하다면 진행하고 불가능하다면 다음 index로 진행. 만약 list의 끝이라면 -1을 return
        tank=0
        index=0
        while index < len(gas):
            if self.can_travel(index, gas*2, cost*2):
                return index
            else:
                index += 1
        return -1
    
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas, total_cost = 0, 0
        current_gas, start_index = 0, 0
        
        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_gas += gas[i] - cost[i]
            
            # 현재 위치에서 가스가 부족하면
            if current_gas < 0:
                # 다음 지점을 새로운 출발 지점으로 설정
                start_index = i + 1
                current_gas = 0
        
        # 전체 가스의 합이 전체 비용의 합보다 작다면 -1을 반환
        if total_gas < total_cost:
            return -1
        else:
            return start_index