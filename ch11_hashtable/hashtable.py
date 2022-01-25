# 해쉬 함수란 임의 크기 데이터를 고정 크기값으로 매핑 할 수 있다.

# 성능이좋다? >> 해시함수 값에 충돌이 최소 , 쉽고 빠른 연산, 해시값이 균일하게 분포, 사용할 키의모든 정보를 이용하여 해싱.

# 해시함수

## 로드팩터 저장공간이 100개가 있을때 80개의 저장된 데이터가 있다면 로드팩터 = 0.8

# 로드팩터가 증가할수록 해시 테이블 성능은 점점 감소.

# key = 넣어야 하는 data // hash func을 통해서 해시값으로 변환을하여 테이블에 저장

#1.개별 체이닝

# 해시값을 계산하여 같은 인덱스로 중복되게 들어왔을경우 그 값뒤에 연결리스트로 이어붙인다.

#2. 오픈 어드레싱  >> 파이썬은 이방식을 쓰고있다. 그 이유는? > 체이닝시에 메모리 할당하는 오버헤드가 높아 오픈 어드레싱을 사용한다.

# 빈곳을 찾아서 들어감. 선형탐사라고도 불린다. >>뭉치게 되어 클러스터링이 문제가됨, 버킷사이즈가 초과되었을경우 삽입할 수 없다.

from hashtable.structures import MyHashTable


def test_hashtable():
    ht = MyHashTable()

    ht.put(1, 1)
    ht.put(2, 2)
    assert ht.get(1) == 1
    assert ht.get(3) == -1

    ht.put(2, 1)
    assert ht.get(2) == 1

    ht.remove(2)
    assert ht.get(2) == -1


def test_birthday_problem():
    import random
    TRIALS = 100000
    same_birthdays = 0

    for _ in range(TRIALS):
        birthdays = []
        for i in range(23):
            birthday = random.randint(1, 365)
            if birthday in birthdays:
                same_birthdays += 1
                break
            birthdays.append(birthday)

    print(f"{same_birthdays / TRIALS * 100}%")


if __name__ == "__main__":
    test_birthday_problem()
    test_hashtable()