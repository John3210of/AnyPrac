# https://school.programmers.co.kr/learn/courses/30/lessons/17684?language=python3 압축

# 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
# 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
# w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
# 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
# 단계 2로 돌아간다.

import string

# 알파벳 리스트 생성
alphabet = list(string.ascii_uppercase)

# 딕셔너리 생성
msg_dict = {}
for i in range(len(alphabet)):
    msg_dict[alphabet[i]] = i + 1

msg='TOBEORNOTTOBEORTOBEORNOT'
# msg='KAKAO'
answer=[]
i=1
val=26
# 첫글자가 있으면 두번째글자까지 확인, ..., n번째 글자까지 확인해서 없으면 단어 추가하고 추가한 곳 전까지 1. answer에 value를 넣는다. 2.단어를 자른다
# 다음 글자가 없으면 그대로 출력하고 끝낸다.
# 자른후에는 다시 i를 초기화한다.
while True:
    if len(msg)==1 or i>100:
        answer.append(msg_dict[msg])
        break
    if msg[:i] in msg_dict:
        i+=1
    else: #사전에 없을경우
        answer.append(msg_dict[msg[:i-1]])
        val+=1
        msg_dict[msg[:i]]=val
        msg=msg[i-1:]
        i=1
print(answer)