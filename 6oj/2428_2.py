import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lst = sorted(map(int, input().split()))
    
    count = 0
    result=0
    for i in range(n-1):
        start = i
        end = n-1
        while start <= end:
            mid = (start + end) // 2
            if lst[i] >= lst[mid]* 0.9:
                result=mid
                start = mid + 1
            else:
                end = mid - 1
        count += result -i
    print(count)