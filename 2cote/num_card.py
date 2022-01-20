# Q2) 숫자 카드 게임
# 숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
# 단, 게임의 룰을 지키며 카드를 뽑아야 하고 룰은 다음과 같다.
# 1. 숫자가 쓰인 카드들이 N X M 형태로 놓여 있다.
# 이때 N은 행의 개수를 의미하며, M은 열의 개수를 의미한다.
# 2. 먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한다.
# 3. 그다음 선택된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑아야 한다.
# 4. 따라서 처음에 카드를 골라낼 행을 선택할 때,
# 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.


# 조건1) n x m 행렬 형태로 입력받기
n, m = map(int, input('n,m의 값을 입력하세요: ').split())
arr = []
small_num = []

for i in range(n):
    arr.append(list(map(int, input().split())))

# 조건2) 뽑고자 하는 행을 설정하기

for i in range(n):
    small_num.append(min(arr[i]))  # >> 행에서 가장 작은 값을 small num list에 넣기
    print(i, '행의 min값', small_num[i])

choice = small_num.index(max(small_num))  # >> small인 값중에 가장 큰값을 구하고 그 index 넘버를 구하기
print(choice,'행을 고른다. output= ',max(small_num)) #>># 조건3) 뽑고자 하는 행에서 가장 작은 숫자 뽑기