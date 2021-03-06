# 문제
# 상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
# 설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.
#
# 상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다. 예를 들어, 18킬로그램 설탕을 배달해야 할 때,
# 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.
#
# 상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline
n = int(input())
# 5의 배수인 경우가 가장 최적화임. 다음으로는 5가 최대한 많으면서 3으로 나누어 떨어져야함 그것도 안돼면 3의 배수여야함.
# 5x+3y = n이 되야함. 여기서 x+y의 최소값을 구해라. 셋중 하나라도 만족 못하면 x+y = -1
# 그렇다면 x+y 값의 리스트 sumXy를 만들어서 min(sumXy)를 한다면? 만약 리스트가 null이라면 -1을 출력
sumXy = []
for x in range(0, 1001):
    for y in range(0, 5000 // 3):
        if 5 * x + 3 * y == n:
            sumXy.append(x + y)

if len(sumXy) == 0:
    print(-1)
else:
    res = min(sumXy)
    print(res)
