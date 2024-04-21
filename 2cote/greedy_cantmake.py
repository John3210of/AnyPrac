n = int(input())

lst = list(map(int, input().split()))
res = [[]]
result = []
if min(lst) != 1:
    print(min(lst) - 1)
else:
    for i in lst:  # res=[[]]
        size = len(res)
        for j in range(size):
            res.append(res[j] + [i])
            print(res)

    for i in range(len(res)):
        for j in range(len(res[i])):
            temp = sum(res[i])
            result.append(temp)

    last = list(set(result))
    for i in range(len(last) - 1):
        if last[i + 1] - last[i] != 1:
            print(last[i]+1)
            break

            ##가득차있을때예외처리해