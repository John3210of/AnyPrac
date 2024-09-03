class Solution:
    def intToRoman(self, num: int) -> str:
        '''
        딕셔너리에 하드코딩으로 두고 파싱 잘 하기?
        자리수를 잘랐을때 4는 1.4로 표현, 9면 1.10으로 표현,나머지는 1~111,5~51 511 5111 이런식으로 표현함
        1. 몇번째 자리수인지 확인하기
        2. 자리수에 맞게 숫자 넣기
        3. 이어붙여서 return 하기
        # 시간복잡도 o(n), 공간복잡도 o(n)
        '''
        int_roman={
            1:'I',
            5:'V',
            10:'X',
            50:'L',
            100:'C',
            500:'D',
            1000:'M'
        }
        num=str(num)
        length=len(num)
        answer=''
        for s in num:
            if 0<int(s)<4:
                answer += int(s)*int_roman[(10**(length-1))]
            elif int(s)==4:
                answer += (int_roman[(10**(length-1))] + int_roman[5*(10**(length-1))])
            elif 4<int(s)<9: # 5,6,7,8
                answer += (int_roman[5*(10**(length-1))]+(int(s)-5)*int_roman[(10**(length-1))])
            elif int(s)==9:
                answer += (int_roman[(10**(length-1))]+int_roman[(10**(length))])
            length -= 1
        return answer
        