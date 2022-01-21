#Q4-2 왕실의 나이트

n=input('입력해: ')

# col=int(n[0]) #ValueError: invalid literal for int() with base 10: 'c'
col=int(ord(n[0]))-96   #ascii code a=97
row=int(n[1])

#상 row-2 하 row+2 좌 col-2 우 col+2
move=[(-2,1),(-2,-1),(2,1),(2,-1),(1,-2),(-1,-2),(1,2),(-1,2)]
cnt=0

for i in move:
    if row+i[0] <= 0 or col+i[1] <= 0:
        continue
    else:
        print(row + i[0])
        print(col + i[1])
        cnt += 1

print('결과:',cnt)


