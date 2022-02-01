import sys

n = int(sys.stdin.readline())
lst = []

for i in range(n):
    lst.append(sys.stdin.readline().strip())
# answer = []
# for i in lst:
#     if i not in answer:
#         answer.append(i)  개느려

lst=list(set(lst))

lst.sort(key=lambda x:(len(x),x))

for i in lst:
    print(i)

# lst = ['asdf', 'sdf', 'sssssss','sssssss']
