n = input()
lst = []
for i in n:
    lst.append(i)
oneM = 0
twoM = 0
flag = 0
last = lst.pop()
while lst:  # 00  11  00
    temp = lst.pop()
    if temp == last:
        continue
    else:
        if flag == 0:
            oneM += 1
            flag = 1
        else:
            twoM += 1
            flag = 0
    last = temp
print(min(oneM, twoM))
