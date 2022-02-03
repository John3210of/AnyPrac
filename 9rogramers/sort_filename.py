files = ["img12.png", "img10.png", "img02.png",
         "img1.png", "IMG01.GIF", "img2.JPG"]
import re

# 정규표현식인가 그걸로 리스트 구간 나눠줘서 리스트 3등분한걸 리스트의 원소로 받고
# 람다로 0,1,2 기준으로 정렬하고 join하면 될듯?

def solution(files):
    temp = []
    answer = []
    for i in files:
        split_str = re.split(r"([0-9]+)", i)  # +는 기준으로나오는거 전부다 엮기
        temp.append(split_str)
    print('머리가슴배: ', temp)

    temp.sort(key=lambda x: (x[0].lower(), int(x[1])))  # 대소문자 관계없음,
                                    # int로 안해주면 숫자를 문자열로봐서 정렬 이상하게 나옴
    print('정렬후', temp)

    for i in temp:
        answer.append(''.join(i))

    print('합체: ', answer)
    return answer


solution(files)
