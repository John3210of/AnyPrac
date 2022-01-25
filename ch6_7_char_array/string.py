if __name__ == "__main__":  #void main() 과 같은 기능
    s ="hello world"
    print(s[1]) #indexing
    print(s[-1]) #indexing revers order
    print(s[1:]) # **slicing**  substring 일부 문자열 추출
    #   위아래가 같은코드다
    print(s[1:len(s)])

    #   slicing
    # [start:end] start는 포함, end는 미포함 >>    start <=  x  <end 을 의미한다.

    print(len(s))

    # :str = type hint 가독성을 높혀준다.
    # type을 지정 하지 않아도 자동으로 받아줌. python

    # string pool이 나오게된 이유? 메모리관리 때문.

    # in 연산자 (문자열안에 문자가 포함되는지?) true,false 반환하는 연산자
    print("s" in "str")

    idx = s.index('l') # return index 함수
    print(idx)

    #list,str 같이 올때 많이씀
    #join : list > str으로 전환  //str 은 불변함수이다. (immutable)

    li=['a','b','c','4']  # li[3]이 4면 int형이라 join 할수없는 에러가 나온다.
    s1 = " ".join(li) # 사이에 무엇을 넣으면서 전환할것인지.
    print(s1)

    #split : str>list로 전환

    #파이선에서 배열(정적) >> 리스트(동적)으로 만들어 진다. 따라서 배열 size가 변할 수 있다.


    #220105 수업 추가

    #정적인 text를 저장하고 싶을때 > string pool 에 저장. 일부요소만 수정하고 싶다면 문제가 생길 수 있다.
    #java의 경우 string buffer로 방지할 수 있다. ?) hello > Hello > hello 로 가면 어떻게 되는지??
    #Deque 는 양방향으로 들어갈수있다. double-ended queue

    #list vs array

    # memory
    # 동적할당 malloc,new(c,java) list(python) >> 사실 동적할당은 정적할당 doubling 한것이다.
    # 정적할당 = 배열의 size가 정해진경우 ex) int arr[5]=[1,2,3,4,5] >> 배열의 이름에는 0번 index의 주소가 들어가 있다.
    # 지역,매개변수

    #브르투 포스 (완전탐색)


