'''
최소공배수 구하고 오름차순 정렬된 순서로 넣는다 > 필요없음 걍 소수의 계산으로 가능함
반열림 구간에 포함되지 않는다면 쭉쭉 넣는다.
'''

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
work_bar = 1/nums[0]
time = 1
for i in range(1,len(nums)):
    time += 1
    work_time = 1/nums[i-1]
    while 1/nums[i] > work_bar:
        time += 1
        work_bar += work_time
time = time + nums[-1]-1
print(time)