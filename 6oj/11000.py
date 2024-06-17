import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())
    lst=[]
    for _ in range(n):
        lst.append(list(map(int,input().split())))
    
    # 강의 끝나는 시간 기준으로 정렬
    lst.sort(key=lambda x:(-x[1],-x[0]))
    class_room=[]
    size=0
    while lst:
        start, end = lst.pop()
        if not class_room:
            class_room.append([start, end])
            size=max(size,len(class_room))
        else:
            # 만약 끝나는 시간의 시간표의 시작시간이 이전 마치는 시간과 같거나 크다면 강의실은 그대로 유지
            # 공존할수없다면 강의장을 하나 추가함. 그때의 마다 강의장 개수 갱신
            for i in range(len(class_room)):
                if class_room[i][1]<=start:
                    class_room[i]=[start,end]
                    break
            else:
                class_room.append([start,end])
                size=max(size,len(class_room))
    print(size)