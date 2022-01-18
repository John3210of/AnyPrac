# #현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
# 예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.
#
# 여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.
#
# 입력
# 첫 줄에 테스트케이스의 수가 주어진다. 각 테스트케이스는 두 줄로 이루어져 있다.
#
# 테스트케이스의 첫 번째 줄에는 문서의 개수 N(1 ≤ N ≤ 100)과, 몇 번째로 인쇄되었는지 궁금한 문서가 현재 Queue에서 몇 번째에 놓여 있는지를 나타내는 정수 M(0 ≤ M < N)이 주어진다.
# 이때 맨 왼쪽은 0번째라고 하자. 두 번째 줄에는 N개 문서의 중요도가 차례대로 주어진다. 중요도는 1 이상 9 이하의 정수이고, 중요도가 같은 문서가 여러 개 있을 수도 있다.
#
# 출력
# 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.
# a=int(input('테스트 횟수: '))
# print('횟수: ',a)
for i in range(1):
    n, m = map(int, input('문서의개수, 인쇄순서가 궁금한 문서: ').split())
    print('문서 갯수,순서가 궁금한 문서(0~ m-1): ', n, m)

    imptc = list(input('중요도: ').split())
    print('중요도 리스트: ', imptc)

    # int 형 list로 형변환

    imptc_int = list(map(int, imptc))
    print('ww', imptc_int)

    cnt = 1
    temp = []

    while cnt < 4:
        # list내의 가장 큰 값을 찾아냄.
        largest = imptc_int[0]
        for j in range(len(imptc_int)):
            if imptc_int[j] > largest:
                largest = imptc_int[j]
                del_len = j
            else:
                del_len = 0
        # index(0)이 가장 크지 않을경우 기존 list에서 제거하고
        # 제거한 부분을 다시 tail에 붙여줌
        if del_len != 0:
            temp.extend(imptc_int[0:del_len])
            del imptc_int[0:del_len]
            imptc_int.extend(temp)
        print('큰수가 가장 먼저 와있니?', imptc_int)

        print_order = []
        print_order.append(imptc_int.pop(0))
        print(print_order)
        cnt += 1
