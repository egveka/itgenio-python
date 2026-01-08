height = [int(i) for i in input().split()]

for i in range(len(height) - 1):
    if height[i] >= height[i + 1]:
        print(height[i])