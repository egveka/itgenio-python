nums = [int(i) for i in input().split()]
n = int(input())
diff = []

for i in range(len(nums)):
    diff.append(abs(n - nums[i]))
m = min(diff)
m_idx = diff.index(m)
print(nums[m_idx])