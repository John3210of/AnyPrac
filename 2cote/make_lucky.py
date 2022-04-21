import sys

inputt = sys.stdin.readline

n = inputt()
length = (len(n) - 1) // 2
n = int(n)
front = list(str(n // (10 ** length)))
back = list(str(n % (10 ** length)))

sumf = 0
sumb = 0
for i in range(len(front)):
    sumf += int(front[i])
    sumb += int(back[i])
if sumf == sumb:
    print('LUCKY')
else:
    print('READY')
