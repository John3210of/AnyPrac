from collections import deque
import math
import sys

sys.setrecursionlimit(100000)


# 문자열을 1개씩 나눠서 리스트에 넣고,
# 리스트 원소끼리 비교해서 같다면 다음것까지 비교하면서 cnt++해준다.
# 만약 다를경우 cnt+문자열을 pop하고 temp에 넣는다. 다시 반복하다가 끝까지 확인하고, join하여
# answer list에 append시키고, 상황을 n//2개씩까지 간후에, 가장짧은 길이의 리스트 원소를 출력해준다.
# abcdddd>a,b,c,d,d,d,d > abc4d
# ab, cd, dd, dd, d > abcd2ddd


def solution(s):
    if len(s) == 1:
        return 1
    def slicing(q, cnt, temp):
        if len(q) <= 1:  # 종료조건
            if cnt > 1:  # 마지막에 연속된 문자가 있을경우 예외처리
                head = str(cnt)
                temp += head + q[0]
            else:
                temp += q[0]
            print(temp)
            return len(temp)
        # [sss] ,cnt=2  > 3s > s
        if q[0] == q[1]:  # 처음원소와 다음원소가 같다면.
            cnt += 1
        else:
            if cnt > 1:
                head = str(cnt)
                temp += head + q[0]
                cnt = 1  # 빼줄때 초기화시킨다.
            else:
                temp += q[0]
        q.popleft()
        return slicing(q, cnt, temp)

    # 리스트 쪼개기
    def uniting(s):
        temp = list(s) #asdf > a,s,d,f
        answer = []
        result = []
        for unit in range(1, len(s) // 2 + 1):  # 몇개씩 나눌건지 => 최대 len//2 개씩 나눌수있다.
            print('문자열길이', len(s))
            print('unit', unit)
            print('횟수', math.ceil(len(s) / unit))
            temp2 = []
            for i in range(math.ceil(len(s) / unit)):  # 몇번 넣을건지
                start = unit * i
                end = start + unit
                if end > len(s):
                    val = ''.join(temp[start:len(s)])
                else:
                    val = ''.join(temp[start:end])
                temp2.append(val)
                print('temp2', temp2)
                print("*" * 25)
            answer.append(temp2)
            print("*" * 25)
            print('answer', answer)
        for i in answer:
            q = deque(i)
            x = slicing(q, 1, '')
            result.append(x)
        # print('result: ', result)
        if not result:
            return 0
        else:
            answer = min(result)
        print(answer)
        return answer
    return uniting(s)


# temp[0:1] temp[1:2] ... temp[] 2(n-1):2n
# temp[0:2] temp[2:4] ... temp[] n(n-1):3n
# 리스트를 어떻게 쪼갤까..


s = 'aabbsdsasd'
print(solution(s))
