# Q30) 중복 문자 없는 가장 긴 문자열

# 문자열 s가 주어지면 문자를 반복하지 않고 가장 긴 부분 문자열의 길이를 찾습니다.
# 제약: # 0 <= 길이 <= 5 * 104   # s는 영문자, 숫자, 기호 및 공백으로 구성됩니다.

# 조건1)문자를 반복하지 않는다.
# 조건2)가장 긴 부분 문자열의 길이를 구한다.

# sol)
#       >> 1.two poiner로 value 중복이 나올때까지 비교한다.
#       >> 2.중복이 나오면 [start:end]  list 길이를 구한다.
#       >> 3.중복 없는 list의 길이를 new list에 append 한다.
#       >> 4.new list를 sort하고 new list[-1] 값을 return한다.


# s = list(input('체크할 문자열을 입력해 주세요: '))
# print(s)

s = 'abcabcbc'
result_length = []
# 시작  #비교시작
# a    b       cabcbb
# 조건1)
for i in range(len(s) - 1):  # start pointer
    for j in range(i + 1, len(s)):  # end pointer
        print('   Start value:', s[i], '[ index', i, '] || end value:', s[j], '[ index', j, ']')
        if s[j] in s[i:j]:  #sol1)
            result_length.append(len(s[i:j]))  # sol2,3)
            print('*  result_length list', result_length)
            print('===============================================================')
            break
result_length.sort()

print('**  최종 result_length list : ', result_length)
  # sol4)
print("중복 문자가 없는 가장 긴 문자열의 길이? = ", result_length[-1])
