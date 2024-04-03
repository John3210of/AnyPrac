# 1. 같은 숫자는 싫어
def solution(arr):
    # arr를 거꾸로 순회하여 stack을 확인하면서 넣어준다.
    # 마지막에 stack을 거꾸로 뒤집어서 반환한다.
    stack=[]
    while arr:
        if not stack or stack[-1] != arr[-1]:
            stack.append(arr.pop())
        else:
            arr.pop()
    return stack[::-1]

# 2.기능 개발
from collections import deque
import math
def solution(progresses, speeds):
    answer = []
    days = deque()
    # 각 기능이 배포되기까지 걸리는 일수 계산하여 days 큐에 저장
    # 첫 번째 기능부터 순서대로 확인하며 배포 처리
    # 기능들 중 배포 가능한 것 확인
    for i in range(len(progresses)):
        remain = math.ceil((100 - progresses[i]) / speeds[i])
        days.append(remain)
    while days:
        count = 1
        first = days.popleft()
        while days and days[0] <= first:
            days.popleft()
            count += 1
        answer.append(count)

    return answer

# 3. 올바른 괄호
def solution(s):
    if s[0] != '(' or s[-1] != ')':
        return False
    # 스택에 넣으면서 쌍을 이룰 수 있는지 확인
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

# 4. 프로세스
from collections import deque
def solution(priorities, location):
    # A B C D E F
    # 1 1 9 1 1 1
    
    #  C D E F A B
    #  9 1 1 1 1 1
    
    # queue => fifo, 꺼내면서 최대값이 나올때까지 꺼내면서 다시 오른쪽으로 붙인다.
    # index가 필요
    # 최대값이 나오면 꺼내고 stack에 붙인다.
    sorted_pri = sorted(priorities)
    queue=deque()
    stack=[]
    for i,v in enumerate(priorities):
        queue.append([i,v])
    while queue:
        temp=queue.popleft()
        if temp[1] != sorted_pri[-1]:
            queue.append(temp)
        else:
            sorted_pri.pop()
            stack.append(temp)
    for i in range(len(stack)):
        if stack[i][0]==location:
            return i+1

# 5. 다리를 지나는 트럭
from collections import deque
def solution(bridge_length, weight, truck_weights):
    # 다리의 길이 = 건너는데 소요되는 시간 = bridge_length
    # 다리의 가용 무게 = weight
    # 택시의 무게 = truck_weights[n]
    # 다리로 들어갈 경우 => 다리가 비었거나, 다리에 있는 무게의합+다음트럭의 무게 <= 가용무게일때
    # 다리에서 빠질경우 => 시간이 트럭이 다리에 들어간 시점으로부터 길이만큼이 지났을 때
    finished=[]
    trucks=len(truck_weights)
    truck_weights = deque(truck_weights)
    report=deque()
    bridge=deque()
    time=0
    while len(finished)!=trucks:
        time+=1
        # 다리에 차가 있고, 뺄 경우를 상정
        if report and time - report[0] >= bridge_length:
            finished.append(report.popleft())
            bridge.popleft()
        # 차가 들어가는 경우 ( 다리에 차가없거나, 다리에 차가있어도 무게가 허용되는 경우)
        if truck_weights and (not bridge or sum(bridge) + truck_weights[0] <= weight):
            bridge.append(truck_weights.popleft())
            report.append(time)
    return time

# 6. 주식가격
def solution(prices):
    answer = [0] * len(prices)
    stack = []
    # 감소했을때, 몇초나 걸렸는지를 우선 저장
    # 감소하지 않은 친구들에 대해서 보상해줌
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer
