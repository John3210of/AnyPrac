n = input()
lst = list(n)
lst2 = list(n)
temp = 0
print(lst)
for i in lst:
    if 58 >= ord(i) >= 48:
        temp += int(i)
        lst2.remove(i)
lst2.sort()
result = ''.join(i for i in lst2)
print(result + str(temp))
# K1KA5CB7
# AJKDLSI412K4JSJ9D
