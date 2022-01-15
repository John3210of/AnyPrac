# Q4. 가장 긴 팰린드롬 문자열?

def longestPalindrom(s):
    # 조건1) 문자열 내에서 팰린드롬 구하기
    # 기준점으로부터 좌우가 같은지 판단하여 같다면 좌우 한칸더 보기
    # 홀수개의 경우.. 가능하지만 짝수개의 팰린드럼이라면 불가능
    # 좌우가 같지 않다면, 문자열 임시저장하고 기준점 이동하기
    # 더이상 좌우가 같은 지점을 못찾을경우, 임시저장값 출력
    # left = 0

    # evenpal =[]
    evenpal = [None] * len(s)
    oddpal = [None] * len(s)

    for i in range(0, len(s)):
        left = i
        # print("i루프수")
        # 2n칸 팰린드롬
        for j in range(i + 1, len(s)):
            if s[left] == s[j]:
                # print("j짝수루프수")
                # Error
                # IndexError: list assignment index out of range
                # evenpal[i] = s[left:j + 1] 빈리스트 생성했는데 i번 인덱스가 어디있는지 찾지 못함.
                # https://stackoverflow.com/questions/5653533/why-does-this-iterative-list-growing-code-give-indexerror-list-assignment-index
                evenpal[i] = s[left:j + 1]
                left -= 1
                # print(evenpal[i])
                if left < 0:
                    break

        # 2n-1칸 팰린드롬
        for j in range(i + 2, len(s)):
            # print("j홀수루프수")
            if s[left] == s[j]:
                oddpal[i] = s[left:j + 1]
                left -= 1
                if left < 0:
                    break

    # 조건2) 가장 긴 팰린드럼 출력하기

    # Error
    # in longestPalindrom     evenmax = max(len(evenpal)) ##
    # TypeError: 'int' object is not iterable
    # evenpal.remove(None)
    # evenpal.remove(None)
    # evenpal.remove(None)
    remove_set = {None}
    # https://latte-is-horse.tistory.com/200 리스트 컴프리헨션
    # allpal = evenpal+oddpal
    evenpal = [i for i in evenpal if i not in remove_set]
    oddpal = [i for i in oddpal if i not in remove_set]
    # max(evenpal, key=lambda s: len(s))

    if len(oddpal) != 0:
        op = len(max(oddpal, key=lambda s: len(s)))  # 한개도 팰린드롬이 없을경우 VALUE ERROR 발생함.
    else:
        op = 0
    if len(evenpal) != 0:
        ep = len(max(evenpal, key=lambda s: len(s)))
    else:
        ep = 0

    if op >= ep:
        print(max(oddpal, key=lambda s: len(s)))
    else:
        print(max(evenpal, key=lambda s: len(s)))


if __name__ == "__main__":
    print('입력: ', end='')
    s = input().split('"')
    string = s[1]

    longestPalindrom(string)
