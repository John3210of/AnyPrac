import sys
input = sys.stdin.readline

def count_less_than_x(x, n):
    '''
    임의의 정수 mid를 가지고, n * n 행렬의 행마다 mid 이하의 값이 몇개인지 센다. 
    1 2 3 4 5 6 ,,, n
    2 4 6 8 10 12 ,,, 2n

    1 2 3 
    2 4 6 > 1,2,3
    3 6 9 > 1,2,3
    i*j<=x 일때 j의 최대값은 x//i 혹은 n (각 행당 n개 초과해서 원소가 존재할 수 없으므로)
    '''
    count = 0
    for i in range(1, n + 1):
        count += min(x // i, n)
    return count
if __name__ == "__main__":
    # 배열을 다 저장시키는건 미친짓일듯
    # n > 행렬의 개수
    # k > 몇번째 수
    # 총 센 개수의 합이 k보다 작다면 k번째수가 아닌셈이므로, 저점을 올린다. 아니라면 고점을 낮춘다.
    # 해서 반환이 되었을때의 mid값이 답이 k번째수?
    n = int(input())
    k = int(input())
    low, high = 1, n * n
    result = 0
    while low <= high:
        mid = (low + high) // 2
        if count_less_than_x(mid, n) < k:
            low = mid + 1
        else:
            result = mid  # mid가 k번째 수가 될 수 있으므로 result를 업데이트
            high = mid - 1
    print(result)