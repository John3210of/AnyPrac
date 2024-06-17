import sys
import heapq
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lst=[]
    for _ in range(n):
        lst.append(list(map(int,input().split())))
    # 강의 끝나는 시간 기준으로 정렬
    # 우선순위큐를 이용하여 끝나는 시간을 가지는 최소힙을 만듬
    # lst를 순회하며 시작 시간이 힙의 head,즉 끝나는 시간보다 크거나 같은경우에는 heap pop and push
    # 그 외의 경우에는 heap push만 하여 힙의 크기를 증가시킨다.
    # 이때 힙 크기의 최대값을 갱신한다.
    lst.sort()
    class_room=[]
    size=0
    class_room.append(lst[0][1])
    for i in range(1,len(lst)):
        if class_room[0]<=lst[i][0]:
            heapq.heappop(class_room)
        heapq.heappush(class_room,lst[i][1])
        size=max(size,len(class_room))
    print(size)