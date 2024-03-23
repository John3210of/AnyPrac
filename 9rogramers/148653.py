# https://school.programmers.co.kr/learn/courses/30/lessons/148653/ 마법의엘리베이터

def solution(storey):
    # 1의 자리부터 생각
    # 5이상은 전부 올리고 자리수 +1,다음자리가 4이하인경우는 빼기(자리수올림x)
    # 마지막인 경우에는 다음자리를 보지않고 끝남
    storey_list=list(map(int,str(storey)))
    count=0
    
    while storey_list:
        temp = storey_list.pop()
        # 1. temp가 6~9일때 >> count += 10-temp, 앞자리가 존재한다면 앞자리의수 1증가
        # 2. temp가 0~4일때 >> count += temp
        # 3. temp가 5일때 >> 앞자리의 수가 0~4일때는 count+=5만
        # 4. temp가 5일때 >> 앞자리의 수가 5~9일때는 count+=5하고, 앞자리의수 1증가
        # 5. temp가 5이고 마지막자리수일때 >> count+=5하고 마무리
        # 마지막자리일때 올림을 하는경우 +1을 해줘야한다.
        if temp > 5:
            count+=10-temp
            if storey_list:
                storey_list[-1] += 1
            else:
                count+=1
        elif temp < 5:
            count+=temp
        else:
            if not storey_list:
                count+=5
            else:
                if storey_list[-1] <5:
                    count+=5
                else:
                    count+=5
                    storey_list[-1]+=1
    return count