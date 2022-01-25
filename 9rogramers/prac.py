# import collections
#
#
# def solution(bridge_length, weight, truck_weights):
#     curweight = 0  # 현재 다리에 올라가 있는 트럭의 무게의 합
#     time = 0  # 시작부터 현재까지 흐른 시간
#     togo = len(truck_weights)  # 움직여야 하는 트럭의 갯수
#     truck_weights += [0]
#     bridge_length  # << 나중에 팝 해야하는데 오류 처리하기 귀찮아서 그냥 붙였어요
#     arrived = 0  # 도착한 트럭의 갯수
#     onbridge = collections.deque([0]bridge_length)  # << 현재 다리의 상태
#     truck_weights = collections.deque(truck_weights)  # queue 형태로 만들어줌.
#     while True:  # << 반복문 들어감
#         time += 1  # 한 바퀴가 1초
#         gone = onbridge.popleft()  # << 무게와 관계 없이 하나가 빠짐.
#         curweight -= gone  # 현재 무게에 빠진 것을 빼 줌. 다리가 비어있으면 0이니까 굳이 if문 안 써줌.
#         if gone != 0:  # << 0이면 빈자리가 빠진 거니까 무시, 0이 아니면 트럭임.
#             arrived += 1  # << arrived += 1
#         if curweight + truck_weights[0] <= weight:  #
#             curweight += truck_weights[0]  # .popleft() == .pop(0)
#             onbridge.append(truck_weights.popleft())  # 대기열에서 빼고 넣음
#         else:
#             onbridge.append(0)
#         if arrived == togo:  # << 도착한 트럭의 갯수가 출발한 트럭의 갯수와 같을 때 break
#             break
#
#     return time
