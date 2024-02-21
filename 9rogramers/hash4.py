phone_book = ["119", "97674223", "1195524421"]

p_dict={}
answer=0
for p in phone_book:
    p_dict[p]=0
for phone in phone_book:
    for k,v in p_dict.items():
        print('phone',phone)
        print('k[:len(phone)]',k[:len(phone)])
        if k != phone and k[:len(phone)] == phone:
            print('im in if loop')
            answer=1
print(answer)


def solution(phone_book):
    p_dict = {}
    phone_book.sort()
    for phone in phone_book:
        for i in range(1, len(phone)):
            prefix = phone[:i]
            if prefix in p_dict:
                return False
        p_dict[phone] = 1
    return True
