import heapq
import sys

input = sys.stdin.readline

# 우선순위큐의 값에 id를 매겨서 이미 삭제되었는지를 확인하는식으로 구현
def solution(Q):
    min_heap = []
    max_heap = []
    visited = [False] * Q
    
    for j in range(Q):
        command, number = input().split()
        number = int(number)
        
        if command == 'I':
            heapq.heappush(min_heap, (number, j))
            heapq.heappush(max_heap, (-number, j))
            visited[j] = True
        
        elif command == 'D':
            if number == 1:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            elif number == -1:
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
    
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if not min_heap or not max_heap:
        return "EMPTY"
    else:
        min_value = min_heap[0][0]
        max_value = -max_heap[0][0]
        return f"{max_value} {min_value}"

if __name__ == "__main__":
    T = int(input().strip())
    results = []
    for _ in range(T):
        Q = int(input().strip())
        result = solution(Q)
        results.append(result)
    print("\n".join(results))
