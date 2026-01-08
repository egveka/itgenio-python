nums = [int(i) for i in input().split()]
sum1 = 0

for i in range(len(nums)):
    if i % 2 == 0:
        sum1 += nums[i]
if len(nums) > 0:
    print(sum1 * nums[0])
else:
    print("0")