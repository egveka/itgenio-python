# Taller than 165

heights = [int(i) for i in input().split()]

for height in heights:
    if height >= 165:
        print(height)