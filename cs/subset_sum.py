# 만약 여러개의 숫자를 원소로 가진 리스트가 있는데, 임의의 원소들을 합해서 특정 수를 구하고자 하려면 어떤 알고리즘이 효과적일까? 
# 원소들의 개수에는 제한이 없고, 합해서 특정 수를 구하기만 하면 된다.

def can_sum(target, numbers):
    dp = [False] * (target + 1)
    dp[0] = True  # 0은 아무것도 선택하지 않음으로 만들 수 있음

    for num in numbers:
        for i in range(num, target + 1):
            if dp[i - num]:
                dp[i] = True
    print(dp)
    return dp[target]

# 예제
numbers = [3, 5, 8]
target = 11
print(can_sum(target, numbers))  # True 출력, 예를 들면 3 + 8 = 11

# 이런 방식의 문제점으로는, 구하고자 하는 숫자가 매우 클 경우, 메모리 문제가 발생할 수 있다.