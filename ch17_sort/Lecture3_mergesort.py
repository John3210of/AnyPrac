def mergesort(lst):

    def scatter(lst):   # 분리시키는 함수
        if len(lst) <= 1:   # 1개씩 분리시킨다.
            return lst

        mid = len(lst) // 2 # 중간 index 기준
        left = lst[0:mid]   # 왼쪽 파트
        right = lst[mid:]   # 오른쪽 파트
        scatter(left)       # 왼쪽 재귀하여 파티션
        scatter(right)      # 오른쪽 재귀하여 파티션

        return merge(scatter(left), scatter(right)) #분리가 끝났다면 merge 함수로 간다.

    def merge(L, R):
        merged_lst = [] # 답을 낼 새로운 배열
        i = j = 0  # 각 L,R의 cursor
        while True:
            if L[i] < R[j]: # cursor 이동하면서 결과 리스트에 append
                merged_lst.append(L[i])
                i += 1
                if i == len(L):
                    merged_lst.extend(R[j:]) # 왼쪽 조각 리스트가 오른쪽보다 먼저 인덱싱이 끝난 경우
                    break
            else:
                merged_lst.append(R[j])
                j += 1
                if j == len(R):
                    merged_lst.extend(L[i:]) # 오른쪽 조각 리스트가 왼쪽보다 먼저 인덱싱이 끝난 경우
                    break

        return merged_lst

    return scatter(lst)


lst = [1, 7, 2, 5, 11, 21, 3, 4, 1111, 0]
print(mergesort(lst))

#
#
#
# lst1 = [1, 1, 2, 3, 5, 6, 10, 12, 14, 15, 222]
# lst2 = [1, 4, 8, 9]
# merge(lst1, lst2)
