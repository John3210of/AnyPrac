lst = [1, 6, 4, 2, 5, 3]

def quicksort(lst, start, end):
    def partition(part, ps, pe):  # part인 list, part start, part end
        pivot = part[pe]  # pivot을 part의 end값으로 초기화
        i = ps - 1  # i = ps-1 => 커서 위치를 초기화
        for j in range(ps, pe):  # ps~pe-1까지, pivot을 제외하고 비교.
            if part[j] <= pivot:  # part[j]를 pivot의 왼편에둘지, 바꾸지 않을지.
                i += 1  # 바꿀 커서 위치를 [-1]부터 한칸씩 +1씩 바꿀자리로 옮겨준다.
                part[i], part[j] = part[j], part[i]  # swap

        part[i + 1], part[pe] = part[pe], part[i + 1]
        # ==>for문이 끝난뒤에 pivot을 구분기준 왼편의+1 요소와 스왑한다.

        return i + 1  # 바뀐 커서위치를 return 한다.

    if start >= end:  # partition 함수가 끝나고나면 start와 end의 위치를 비교해서 끝낼지 재귀할지 정한다.
        return None

    p = partition(lst, start, end)  # 변수 p에 partition의 리턴값을 저장한다.=>바뀐 커서위치인 i+1
    quicksort(lst, start, p - 1)  # start,i를 가지고 재귀한다.
    quicksort(lst, p + 1, end)

    print(lst)
    return lst


quicksort(lst, 0, -1)
