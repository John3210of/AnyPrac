def letterCombinations(digits):

    def make_letter(idx, letter):
        print('idx:',idx)
        print('letter:',letter)
        # base condition
        if idx == len(digits):
            ans.append(letter)
            return
        # dfs 깊이 별로(번호 2 -> 3) 가능한 모든 조합 호출
        for i in phone_keyboard[digits[idx]]:
            make_letter(idx + 1, letter + i)

    ans = []
    # example 2
    if not digits:
        return ans
    phone_keyboard = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                      '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                      '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'],
                      '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
    # 초기 상태 전달
    make_letter(0, "")
    print(ans)
    return ans


##아이디어:
# 각 숫자는 여러 문자 중 하나를 의미할 수 있으므로 입력 숫자 문자열(D)을 반복할 때 다른 경로로 분기하는 코드를 만들어야 합니다.
# 이것은 문자의 각 순열을 확인하고 응답 배열(ans)에 저장하므로 깊이 우선 검색(DFS) 접근 방식이 필요합니다.
# DFS 접근 방식의 경우 여러 옵션 중 하나를 사용할 수 있지만 일반적으로 재귀 솔루션이 가장 깨끗합니다.
# 그러나 먼저 숫자를 가능한 문자로 변환하기 위해 조회 테이블(L)을 설정해야 합니다.
# 숫자는 실제로 인덱스가 낮은 정수이므로 여기서는 거의 차이 없이 배열 또는 맵/사전 중에서 실제로 선택할 수 있습니다.
# DFS 함수(dfs)의 경우 D의 현재 위치(pos)와 빌드 중인 문자열(str)을 제공해야 합니다. 이 함수는 D, L 및 ans에도 액세스할 수 있어야 합니다.
# DFS 기능 자체는 매우 간단합니다. 완료된 str을 ans로 푸시하고, 그렇지 않으면 현재 위치와 일치하는 문자를 찾은 다음 각 경로에서 새로운 재귀 함수를 실행합니다.
# 작업이 끝나면 as를 반환할 준비가 되어 있어야 합니다.

L = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl",
     '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}


def letterCombinations2(D):
    lenD, ans = len(D), []
    if D == "": return []

    def dfs(pos, st):
        if pos == lenD:
            ans.append(st)
        else:
            letters = L[D[pos]]
            for letter in letters:
                dfs(pos + 1, st + letter)

    dfs(0, "")
    print(ans)
    return ans

if __name__ == "__main__":
    letterCombinations('234')
    letterCombinations2('234')