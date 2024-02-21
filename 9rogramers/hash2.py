nums = [3,3,3,2,2,4]
nums = [3,1,2,3]

quantity = int(len(nums)/2)

if len(nums)==1:
    answer=1
elif quantity <= len(set(nums)):
    answer=quantity
else:
    answer=len(set(nums))

print(answer)