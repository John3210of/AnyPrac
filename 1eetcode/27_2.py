lst=[0,1,2,2,3,0,4,2]

val = 2
while val in lst:
    lst.remove(val)
    print(lst)
print("*"*20)
print(lst)