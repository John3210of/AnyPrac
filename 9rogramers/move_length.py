def solution(dirs):
    mypos = [5, 5]
    cnt = 0

    # 로직2) route값을 저장해야함.
    # route=[None]*len(dirs)*2

    route = []

    # x>nx로 간 정보를 리스트로 저장해서 리스트안에 없다면 cnt++
    # 로직3) dirs[i]에 대한 딕셔너리 생성 U:(1,0) ... 이런식으로

    move = {  # row col
        'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]
    }

    dirs = list(dirs)

    for i in range(len(dirs)):  # 이동
        c_row = str(mypos[0])
        c_col = str(mypos[1])
        temp1 = c_row + c_col
        print('이동전', mypos)

        mypos[0] = mypos[0] + move[dirs[i]][0]  # row = y
        mypos[1] = mypos[1] + move[dirs[i]][1]  # col = x

        # 로직4) 만약 그래프 바깥이면 이동하지 않음

        print('이동후', mypos)
        if mypos[0] < 0 or mypos[0] > 10 or mypos[1] < 0 or mypos[1] > 10:
            print('안대')
            mypos[0] = mypos[0] - move[dirs[i]][0]      #다시 원점으로 돌려줌
            mypos[1] = mypos[1] - move[dirs[i]][1]
            continue

        # 로직5) 가지 않은 길이면 cnt++, 이미 갔던길 cnt하지않고 이동. ### 몰???루

        c_row = str(mypos[0])
        c_col = str(mypos[1])
        temp2 = c_row + c_col  # temp1=이동전 좌표, temp2=이동후 좌표
        if [temp1, temp2] in route or [temp2, temp1] in route:
            continue

        route.append([temp1, temp2])
        route.append([temp2, temp1])
        print('route: ', route)
        cnt += 1

    answer = cnt
    print('이동한 횟수: ', cnt)
    return answer


dirs = 'UUUUUUUU'

solution(dirs)

##################################################################################
#
# from collections import defaultdict
#
#
# def solution(dirs):
#     mypos = [5, 5]
#     cnt = 0
#     # 로직1) 11 X 11 좌표평면 배열 생성.
#     graph = [[[0] for col in range(11)] for row in range(11)]
#     # 로직2) 11 X 11 visited 배열 생성. 굳이?
#     # 로직2.1) route값을 저장해야함.
#     route = defaultdict(list)
#     # x>nx로 간 정보를 리스트로 저장해서 리스트안에 없다면 cnt++
#     # 로직3) dirs[i]에 대한 딕셔너리 생성 U:(1,0) ... 이런식으로
#     move = {  # row col
#         'U': [-1, 0], 'D': [1, 0], 'R': [0, 1], 'L': [0, -1]
#     }
#
#     dirs = list(dirs)  # for문에 돌리려고 list화함.
#     for i in range(len(dirs)):  # 이동
#         # "ULURRDLLU"
#         mypos[0] = mypos[0] + move[dirs[i]][0]  # row = y
#         mypos[1] = mypos[1] + move[dirs[i]][1]  # col = x
#         # 로직4) 만약 배열 바깥이면 이동하지 않음
#         if mypos[0] < 0 or mypos[0] > 10 or mypos[1] < 0 or mypos[1] > 10:
#             continue
#         # 로직5) 가지 않은 길이면 cnt++, 이미 갔던길 cnt하지않고 이동. ### 몰???루
#         # 이중딕셔너리가 가능하다면 pos1 > pos2 의 xy좌표를 기억해서 딕셔너리로 route에 넣을수 있지 않을까?
#         #  route={ edge1:{ 'pos_before_move': [0,0] , 'pos_after_move':[0,1] },
#         #          edge2:{ 'pos_before_move': [0,1] , 'pos_after_move':[1,1] }
#         #         }
#         #
#         cnt += 1
#
#     print(mypos[1] - 5, -mypos[0] + 5)  # x,y 좌표로 보기
#     print(cnt)
#
#     # return cnt(=answer)
#
#     answer = 0
#     return answer