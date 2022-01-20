# b_lens = 2
# w = 10
# truck_weights = [7, 4, 5, 6]
# lens = len(truck_weights)
# truck_weights.reverse()  # 대기중인 트럭
# t_aft = []  # 다리를 통과한 트럭
# cur_brg = [0]  # 현재 다리에 올라간 트럭
# time = 0  # 현재 시간
# temp = []  # n번 트럭이 들어간 시간
#
# while len(t_aft) < lens:
#     try:
#         if sum(cur_brg) + truck_weights[-1] <= 10:
#             time += 1
#             cur_brg.append(truck_weights.pop())
#             temp.append(time)
#         else:
#
#                 print('시간 증가 보기',time)
#
#             cur_brg.reverse()
#             t_aft.append(cur_brg.pop())
#         print(temp)
#         print('경과 시간', time)
#         print('다리를 건너는 트럭', cur_brg)
#         print('다리를 지난 트럭', t_aft)
#     except IndexError:
#         pass
#
# print(cur_brg)
#
# answer = time

############################################################################
from collections import deque

bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]

############################################################################

truck_weights = deque(truck_weights) #deque
bridge = deque([0 for _ in range(bridge_length)]) #bridge 에 트럭이 없다면 길에 0을 넣는 생각
time = 0
bridge_weight = 0
while len(bridge) != 0:
    out = bridge.popleft()         #popleft후에 빠진 무게를 bridge_weight에 갱신
    bridge_weight -= out
    time += 1
    if truck_weights:              # **is not None list**
        if bridge_weight + truck_weights[0] <= weight:  #대기열 첫째 무게와 현재 다리의 무게를 더해서 가능한 무게 이하인경우
            left = truck_weights.popleft()              #대기열 첫번째 index를 bridge로 append, 무게 갱신한다.
            bridge_weight += left
            bridge.append(left)
        else:
            bridge.append(0)                            #불가능할경우 트럭대신 0 을 넣어줌
                                ## 왼쪽으로부터 빼고 조건문돌고 오른쪽으로 넣고. 이미 0이 들어간것으로 생각하는 접근방법
                                ## 값이 없다라고 생각하고 접근하는 방법이 쉽지 않았다.
print(time)